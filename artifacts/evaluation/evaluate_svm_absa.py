import pandas as pd
import os
import joblib
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model_path, data_path, output_dir):
    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)
    
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    X = df['ulasan']
    y = df['sentiment']
    
    print("Making predictions...")
    y_pred = model.predict(X)
    
    print("\nClassification Report:")
    report = classification_report(y, y_pred)
    print(report)
    
    # Save report
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "evaluation_report.txt"), "w") as f:
        f.write(report)
        
    # Confusion Matrix Plot
    cm = confusion_matrix(y, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=model.classes_, yticklabels=model.classes_)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig(os.path.join(output_dir, "confusion_matrix.png"))
    print(f"Confusion matrix saved to {output_dir}")

if __name__ == "__main__":
    model_dir = os.path.join("artifacts", "model")
    clean_dir = os.path.join("data", "clean")
    eval_dir = os.path.join("artifacts", "evaluation", "assets")
    
    # Find latest model and data
    models = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]
    data_files = [f for f in os.listdir(clean_dir) if f.endswith(".csv")]
    
    if not models or not data_files:
        print("Model or data files missing.")
    else:
        latest_model = sorted(models)[-1]
        latest_data = sorted(data_files)[-1]
        
        evaluate_model(
            os.path.join(model_dir, latest_model),
            os.path.join(clean_dir, latest_data),
            eval_dir
        )
