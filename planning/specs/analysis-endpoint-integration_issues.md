# Analysis Endpoint Model Integration

## 1. Big View & Features
- **Goal**: Integrate the pre-trained ABSA Support Vector Machine (SVM) pipeline into the FastAPI backend so that the analysis endpoint returns real predictions instead of mock data.
- **Features**:
  - Load the scikit-learn pipeline `svm_absa_pipeline_2026-05-08.pkl` from the `artifacts/model/` directory.
  - Implement **lazy-loading** for the ML model in `AnalysisService` to prevent slow server startups and reloading during development.
  - Map the raw model predictions into the `AnalysisResult` Pydantic schemas.
  - Handle potential errors gracefully (e.g., model file not found).

## 2. Component Updates

### 2.1 `src/analysis/service.py`
- Update the `AnalysisService` class to lazily load the `.pkl` file using `joblib`.
- Modify `analyze_review` to use the loaded model:
  - Input: raw text string (product review).
  - Processing: Call the predict method on the pipeline.
  - Output: `List[AnalysisResult]` where each result contains an extracted aspect and its predicted sentiment.

### 2.2 Model Loading Strategy
- Because loading `spacy` and `scikit-learn` models is heavy, we will NOT load the model in the global scope or `__init__`.
- We will use lazy loading: load the model on the first request to the `analyze_review` method. This keeps the server startup fast.

## 3. Implementation Steps
1. **Update Imports**: Ensure `joblib` and `os` are imported in `src/analysis/service.py`. (DONE)
2. **Model Path**: Define the path to `artifacts/model/svm_absa_pipeline_2026-05-08.pkl` relative to the project root. (DONE)
3. **Modify `AnalysisService`**: (DONE)
   - Add an attribute `_model = None` to hold the loaded model.
   - Create a method `_load_model_if_needed(self)` that checks if `self._model` is `None`. If it is, use `joblib.load()` to load it.
   - Update `analyze_review` to call `_load_model_if_needed()` and pass the `review_text` through `self._model.predict()`.
   - Parse the pipeline's output. (Assuming the pipeline returns a list of dictionaries or tuples with aspect and sentiment).
4. **Error Handling**: Use `try-except` blocks. If model loading or prediction fails, raise a relevant error or log it and return a default/fallback response. (DONE)
5. **Testing**: (IN PROGRESS)
   - Start the FastAPI server.
   - Send a request to `POST /api/analyze`.
   - Verify that real ML predictions are returned.
