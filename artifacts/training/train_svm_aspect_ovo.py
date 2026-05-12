import pandas as pd
import os
import joblib
from datetime import datetime
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

def train_aspect_model(train_path, test_path, model_path):
    print(f"Loading data from {train_path} and {test_path}...")
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    
    # Drop rows with missing aspects or ulasan
    df_train = df_train.dropna(subset=['ulasan', 'aspect'])
    df_test = df_test.dropna(subset=['ulasan', 'aspect'])

    X_train = df_train['ulasan']
    y_train = df_train['aspect']
    X_test = df_test['ulasan']
    y_test = df_test['aspect']

    print("Building pipeline with OneVsOneClassifier...")
    # Using OneVsOneClassifier as requested by user based on Hsu and Lin paper
    # One-vs-One trains K(K-1)/2 classifiers and uses a voting scheme.
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
        ('clf', OneVsOneClassifier(SVC(probability=True, kernel='linear')))
    ])

    # Hyperparameter tuning
    param_grid = {
        'clf__estimator__C': [0.1, 1, 10],
        'tfidf__max_features': [1000, 2000, None]
    }

    print("Starting Grid Search...")
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
    grid_search.fit(X_train, y_train)

    print(f"Best parameters: {grid_search.best_params_}")
    best_model = grid_search.best_estimator_

    # Evaluation
    print("Evaluating model...")
    y_pred = best_model.predict(X_test)
    
    from sklearn.metrics import accuracy_score, f1_score
    
    acc = accuracy_score(y_test, y_pred)
    weighted_f1 = f1_score(y_test, y_pred, average='weighted')
    macro_f1 = f1_score(y_test, y_pred, average='macro')
    
    report = classification_report(y_test, y_pred)
    
    evaluation_text = (
        f"Model: {os.path.basename(model_path)}\n"
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'='*30}\n"
        f"Accuracy: {acc:.4f}\n"
        f"Weighted F1: {weighted_f1:.4f}\n"
        f"Macro F1: {macro_f1:.4f}\n"
        f"{'='*30}\n"
        f"Classification Report:\n{report}"
    )
    
    print("\n" + evaluation_text)

    # Save evaluation results
    eval_dir = os.path.join("artifacts", "evaluation", "aspect")
    os.makedirs(eval_dir, exist_ok=True)
    
    with open(os.path.join(eval_dir, "aspect_classification_report.txt"), "w") as f:
        f.write(evaluation_text)
    
    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(best_model, model_path)
    print(f"Aspect model saved to {model_path}")

if __name__ == "__main__":
    # Work from project root
    clean_dir = os.path.join("data", "clean")
    model_dir = os.path.join("artifacts", "model")
    
    # Find the latest cleaned files
    train_files = [f for f in os.listdir(clean_dir) if f.endswith("_train.csv")]
    test_files = [f for f in os.listdir(clean_dir) if f.endswith("_test.csv")]
    
    if not train_files or not test_files:
        print(f"No cleaned data found in {clean_dir}")
    else:
        # Sort to get the latest based on date in filename
        latest_train = sorted(train_files)[-1]
        latest_test = sorted(test_files)[-1]
        
        train_path = os.path.join(clean_dir, latest_train)
        test_path = os.path.join(clean_dir, latest_test)
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        model_name = f"svm_aspect_pipeline_{date_str}.pkl"
        model_path = os.path.join(model_dir, model_name)
        
        train_aspect_model(train_path, test_path, model_path)
