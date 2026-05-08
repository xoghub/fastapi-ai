# Initial Project and Machine Learning Setup

## 1. Big View & Features
- **Goal**: Create an Aspect-Based Sentiment Analysis (ABSA) model to process raw marketplace product reviews, extract specific product features (aspects), and determine the sentiment polarity (Positive/Negative/Neutral) associated with each.
- **Features**:
  - Train a lightweight machine learning classifier from scratch.
  - Perform robust text preprocessing and feature extraction on raw review data.

## 2. Technology Stack
- **Machine Learning**: Python (Scikit-Learn, Pandas, Spacy, NLTK)
- *(Note: Frontend and Backend planning are skipped for this issue as requested.)*

## 3. Naming Conventions & Project Structure
- **Planning**: `planning/specs/feature-name_issues.md`
- **Models**: `artifacts/model/model_architecture_version_YYYY-MM-DD.pkl`
- **ML Code**: `artifacts/training/[code-name].py`, `artifacts/preprocessing/[code-name].py`, `artifacts/evaluation/[code-name].py`
- **Data**: `data/raw/scraped-data_YYYY-MM-DD.csv`, `data/clean/scraped-data_YYYY-MM-DD_cleaned_YYYY-MM-DD.csv`

## 4. Machine Learning Planning
- **Method or Architecture**: Two-stage Pipeline Model (Aspect Extraction -> Sentiment Classification).
  - *Stage 1 (Aspect Extraction)*: Linguistic Rule-Based extraction using Dependency Parsing.
  - *Stage 2 (Sentiment Classification)*: Support Vector Machine (SVM) utilizing TF-IDF.
- **Reason**: This provides a lightweight, simpler model while still incorporating deep hierarchical linguistic understanding required by advanced ABSA research papers (like *Hierarchical Model Reviews for ABSA*).

### 4.1 Data Preprocessing Implementation Steps (For execution by agent)
- **Step 1: Basic Cleaning**
  - Read CSV from `data/raw/`.
  - Create a python function to lowercase text, remove HTML tags using regex, convert emojis to text, and remove special characters.
- **Step 2: Linguistic Parsing**
  - Load the `en_core_web_sm` model from `spacy`.
  - Process each review to assign Part-of-Speech (POS) tags to every word.
  - Run Dependency Parsing to find relationships (e.g., finding the adjective describing a noun).
- **Step 3: Normalization**
  - Extract the `lemma_` attribute from spacy tokens to reduce words to their root forms.
  - Save the resulting cleaned dataset to `data/clean/`.

### 4.2 Feature Engineering Implementation Steps (For execution by agent)
- **Step 1: TF-IDF Vectorization**
  - Initialize `TfidfVectorizer` from `sklearn.feature_extraction.text`.
  - Fit the vectorizer on the cleaned text to extract unigram and bigram features.
- **Step 2: Syntactic & Lexicon Features**
  - Write a function that calculates the distance between the extracted aspect term (Noun) and sentiment word (Adjective) in the Spacy dependency tree.
  - (Optional but recommended) Map the sentiment words against the VADER sentiment lexicon to get a baseline polarity score.

### 4.3 Training Process Implementation Steps (For execution by agent)
- **Step 1: Data Split**
  - Use `train_test_split` from `sklearn.model_selection`.
  - Split data 80% for training and 20% for testing. Set `stratify=y` to ensure balanced sentiment classes.
- **Step 2: Pipeline Training**
  - Define a Scikit-Learn `Pipeline` combining the `TfidfVectorizer` and the `SVC` (Support Vector Classifier).
  - Train the pipeline on the 80% training set.
- **Step 3: Hyperparameter Tuning**
  - Initialize `GridSearchCV`.
  - Set parameter grid for SVM (e.g., `C: [0.1, 1, 10]`, `kernel: ['linear', 'rbf']`).
  - Fit the grid search to find the optimal model.

### 4.4 Evaluation Process Implementation Steps (For execution by agent)
- **Step 1: Metrics Calculation**
  - Predict on the 20% test set.
  - Use `classification_report` from `sklearn.metrics` to output Accuracy, Precision, Recall, and Macro F1-Score.
- **Step 2: Error Analysis**
  - Generate a confusion matrix using `confusion_matrix`. If the F1-score is below 80%, identify which class (e.g., Neutral) is dragging down the score and adjust class weights in the SVM.
- **Step 3: Save Artifacts**
  - Use `joblib` or `pickle` to save the best model from the Grid Search to `artifacts/model/svm_absa_pipeline_YYYY-MM-DD.pkl`.
  - Save the classification report text file and confusion matrix plot to `artifacts/evaluation/`.
