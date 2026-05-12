import pandas as pd
import os
import joblib
from sklearn.metrics import classification_report, accuracy_score, f1_score
from datetime import datetime

def evaluate_aspect_model(model_path, data_path, output_dir):
    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)
    
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # Drop rows with missing values
    df = df.dropna(subset=['ulasan', 'aspect'])
    
    X = df['ulasan']
    y = df['aspect']
    
    print("Making predictions...")
    y_pred = model.predict(X)
    
    acc = accuracy_score(y, y_pred)
    weighted_f1 = f1_score(y, y_pred, average='weighted')
    macro_f1 = f1_score(y, y_pred, average='macro')
    
    report = classification_report(y, y_pred)
    
    evaluation_text = (
        f"Model: {os.path.basename(model_path)}\n"
        f"Data: {os.path.basename(data_path)}\n"
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'='*30}\n"
        f"Accuracy: {acc:.4f}\n"
        f"Weighted F1: {weighted_f1:.4f}\n"
        f"Macro F1: {macro_f1:.4f}\n"
        f"{'='*30}\n"
        f"Classification Report:\n{report}"
    )
    
    print("\n" + evaluation_text)
    
    # Save report
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "aspect_evaluation_report.txt")
    with open(report_path, "w") as f:
        f.write(evaluation_text)
    print(f"Evaluation report saved to {report_path}")

if __name__ == "__main__":
    # Work from project root
    model_dir = os.path.join("artifacts", "model")
    clean_dir = os.path.join("data", "clean")
    eval_dir = os.path.join("artifacts", "evaluation", "assets", "aspect")
    
    # Find latest aspect model
    aspect_models = [f for f in os.listdir(model_dir) if f.startswith("svm_aspect_pipeline") and f.endswith(".pkl")]
    test_files = [f for f in os.listdir(clean_dir) if f.endswith("_test.csv")]
    
    if not aspect_models or not test_files:
        print("Required model or test data files missing.")
    else:
        latest_model = sorted(aspect_models)[-1]
        latest_test = sorted(test_files)[-1]
        
        evaluate_aspect_model(
            os.path.join(model_dir, latest_model),
            os.path.join(clean_dir, latest_test),
            eval_dir
        )
