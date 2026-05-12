# Analysis Endpoint Model Integration

## 1. Big View & Features
- **Goal**: Integrate the pre-trained ABSA Support Vector Machine (SVM) pipeline into the FastAPI backend so that the analysis endpoint returns real predictions instead of mock data.
- **Features**:
  - Load the scikit-learn pipeline `svm_absa_pipeline_2026-05-08.pkl` (for sentiment prediction) and the new multiclassification model `svm_aspect_pipeline_2026-05-11.pkl` (for aspect prediction) from the `artifacts/model/` directory.
  - Implement **lazy-loading** for both ML models in `AnalysisService` to prevent slow server startups and reloading during development.
  - Map the raw model predictions into the `AnalysisResult` Pydantic schemas, combining the aspect from the new model and sentiment from the old model.
  - Handle potential errors gracefully (e.g., model file not found).

## 2. Component Updates

### 2.1 `src/analysis/service.py`
- Update the `AnalysisService` class to lazily load the two `.pkl` files using `joblib`.
- Modify `analyze_review` to use the loaded models:
  - Input: raw text string (product review).
  - Processing: Call the predict method on the aspect pipeline to get the aspect, and on the sentiment pipeline to get the sentiment.
  - Output: `List[AnalysisResult]` where each result contains the aspect predicted by the new model and the sentiment predicted by the old model.

### 2.2 Model Loading Strategy
- Because loading `spacy` and `scikit-learn` models is heavy, we will NOT load the models in the global scope or `__init__`.
- We will use lazy loading: load both models on the first request to the `analyze_review` method. This keeps the server startup fast.

## 3. Implementation Steps
1. **Update Imports**: Ensure `joblib` and `os` are imported in `src/analysis/service.py`. (DONE)
2. **Model Paths**: Define the paths to `artifacts/model/svm_absa_pipeline_2026-05-08.pkl` (sentiment) and `artifacts/model/svm_aspect_pipeline_2026-05-11.pkl` (aspect) relative to the project root. (DONE)
3. **Modify `AnalysisService`**: (DONE)
   - Add attributes `_sentiment_model = None` and `_aspect_model = None` to hold the loaded models.
   - Create a method `_load_models_if_needed(self)` that checks if the models are `None` and loads them via `joblib.load()`.
   - Update `analyze_review` to call `_load_models_if_needed()` and pass the `review_text` through both `_aspect_model.predict()` and `_sentiment_model.predict()`.
   - Parse the pipelines' outputs to combine them into the final response.
4. **Error Handling**: Use `try-except` blocks. If model loading or prediction fails, raise a relevant error or log it and return a default/fallback response. (DONE)
5. **Testing**: (IN PROGRESS)
   - Start the FastAPI server.
   - Send a request to `POST /api/analyze`.
   - Verify that real ML predictions are returned.

## 4. API Endpoint Definition

### `POST /api/analyze`
**Description**: Analyzes a product review to extract the aspect and sentiment using two separate pre-trained ML models.

#### Request Headers
- `Content-Type`: `application/json`

#### Request Body
```json
{
  "review_text": "suara speakernya jernih dan bassnya kerasa banget"
}
```

#### Good Response (200 OK)
```json
{
  "review_text": "suara speakernya jernih dan bassnya kerasa banget",
  "analysis": [
    {
      "aspect": "suara",      // Outcome from new multiclassification model (svm_aspect_pipeline_2026-05-11.pkl)
      "sentiment": "Positive" // Outcome from old sentiment model (svm_absa_pipeline_2026-05-08.pkl)
    }
  ]
}
```

#### Error Response (500 Internal Server Error)
```json
{
  "detail": "Failed to load ML models or perform inference."
}
```
