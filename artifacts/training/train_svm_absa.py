import pandas as pd
import os
import joblib
from datetime import datetime
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

def train_model(input_path, model_path):
    print(f"Loading cleaned data from {input_path}...")
    df = pd.read_csv(input_path)
    
    if df.empty:
        print("Error: Cleaned data is empty.")
        return

    # Use 'ulasan' as features and 'sentiment' as target
    # Note: This simple model predicts sentiment. A more complex ABSA might predict both aspect and sentiment.
    X = df['ulasan']
    y = df['sentiment']

    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Building pipeline...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
        ('svm', SVC(probability=True))
    ])

    # Hyperparameter tuning
    param_grid = {
        'svm__C': [0.1, 1, 10],
        'svm__kernel': ['linear', 'rbf'],
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
    
    print("\nClassification Report:")
    report = classification_report(y_test, y_pred)
    print(report)

    # Save evaluation results
    eval_dir = os.path.join("artifacts", "evaluation")
    os.makedirs(eval_dir, exist_ok=True)
    
    with open(os.path.join(eval_dir, "classification_report.txt"), "w") as f:
        f.write(report)
    
    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(best_model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    # Define paths
    clean_dir = os.path.join("data", "clean")
    model_dir = os.path.join("artifacts", "model")
    
    # Find the latest cleaned file
    files = [f for f in os.listdir(clean_dir) if f.endswith("_train.csv")]
    if not files:
        print(f"No cleaned data found in {clean_dir}")
    else:
        # Sort by filename (which contains dates)
        latest_file = sorted(files)[-1]
        input_path = os.path.join(clean_dir, latest_file)
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        model_name = f"svm_absa_pipeline_{date_str}.pkl"
        model_path = os.path.join(model_dir, model_name)
        
        train_model(input_path, model_path)
