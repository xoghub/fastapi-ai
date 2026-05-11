# Aspect Prediction Model Integration

## 1. Big View & Features
- **Goal**: Update the machine learning pipeline to predict aspects from text reviews. The current model only predicts sentiment, and the application server relies on simple keyword matching for aspect extraction. A multi-label machine learning model will yield more robust and accurate aspect predictions.
- **Features**:
  - Preprocess and label training data for multi-label aspect classification.
  - Train a multi-label classification model (e.g., using Support Vector Machines).
  - Integrate the new model into the `AnalysisService` so that both aspects and sentiments are predicted via ML.

## 2. Machine Learning Details
- **Model Architecture**:
  - We will use a `Pipeline` containing a `TfidfVectorizer` for text feature extraction and a `OneVsOneClassifier` wrapping an `SVC` (Support Vector Classifier).
  - **Reason and Explanation**: We are framing aspect prediction as a multiclass classification problem (predicting the primary aspect). Based on Hsu and Lin's research (https://www.csie.ntu.edu.tw/~cjlin/papers/multisvm.pdf), the One-vs-One (OVO) method is highly effective for multiclass Support Vector Machines, often providing faster training times and competitive accuracy compared to One-vs-Rest.
- **Input Data Description**: Cleaned text reviews (strings).
- **Output Data Description**: A single categorical class label indicating the dominant aspect (e.g., `suara`, `packing`, `pengiriman`, `harga`, `bass`).
- **Training Data**: 
  - We will use the existing cleaned data in `data/clean/`. 
  - If aspect labels are missing, we will write a preprocessing script in `artifacts/preprocessing/` to bootstrap aspect labels using our existing keyword mapping, which will serve as a starting point.
- **Evaluation Metrics**:
  - Multiclass Accuracy.
  - Weighted and Macro-F1 scores to handle potential class imbalances among aspects.
- **Training Process**:
  - Extract text features using TF-IDF.
  - Train the multi-output SVM.
  - Perform GridSearchCV for hyperparameter tuning.
- **Evaluation Result**: (To be filled after training and evaluation)
- **Save Model Location**: `artifacts/model/svm_aspect_pipeline_YYYY-MM-DD.pkl`

## 3. Integration Plan
- Update `app-server/src/analysis/service.py` to lazy-load the new aspect prediction model alongside the sentiment model (or load a single joint model if combined).
- Replace the keyword-matching heuristic in `analyze_review` with a call to the aspect model's `predict()` method.
- Return the predicted aspects and their corresponding sentiments.
