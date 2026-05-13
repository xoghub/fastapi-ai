import logging
import os
from typing import List
import joblib
from fastapi.concurrency import run_in_threadpool
from src.analysis.schemas import AnalysisResult

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self._sentiment_model = None
        self._aspect_model = None
        # Paths to models relative to project root
        base_dir = os.path.dirname(__file__)
        self._sentiment_model_path = os.path.normpath(
            os.path.join(
                base_dir,
                "..",
                "..",
                "..",
                "artifacts",
                "model",
                "svm_absa_pipeline_2026-05-08.pkl",
            )
        )
        self._aspect_model_path = os.path.normpath(
            os.path.join(
                base_dir,
                "..",
                "..",
                "..",
                "artifacts",
                "model",
                "svm_aspect_pipeline_2026-05-11.pkl",
            )
        )

        # Aspect keywords mapping based on Indonesian training data
        self._aspect_keywords = {
            "suara": ["suara", "jernih", "bunyi", "audio", "speaker", "jerni"],
            "packing": ["packing", "pack", "bungkus", "kemasan", "bubble wrap", "rapi"],
            "pengiriman": [
                "pengiriman",
                "kirim",
                "sampai",
                "datang",
                "kurir",
                "proses",
                "cepat",
            ],
            "harga": ["harga", "worth it", "murah", "mahal", "biaya", "duit", "worthit"],
            "bass": ["bass", "ngebass", "ngebasss"],
        }

    async def _load_models_if_needed(self):
        """Lazily load both models in a threadpool to avoid blocking the event loop."""
        if self._sentiment_model is None:
            if not os.path.exists(self._sentiment_model_path):
                logger.error(f"Sentiment model file not found at {self._sentiment_model_path}")
            else:
                try:
                    logger.info(f"Loading sentiment model from {self._sentiment_model_path}...")
                    self._sentiment_model = await run_in_threadpool(joblib.load, self._sentiment_model_path)
                    logger.info("Sentiment model loaded successfully.")
                except Exception as e:
                    logger.error(f"Failed to load sentiment model: {str(e)}")

        if self._aspect_model is None:
            if not os.path.exists(self._aspect_model_path):
                logger.error(f"Aspect model file not found at {self._aspect_model_path}")
            else:
                try:
                    logger.info(f"Loading aspect model from {self._aspect_model_path}...")
                    self._aspect_model = await run_in_threadpool(joblib.load, self._aspect_model_path)
                    logger.info("Aspect model loaded successfully.")
                except Exception as e:
                    logger.error(f"Failed to load aspect model: {str(e)}")

    async def analyze_review(self, review_text: str) -> List[AnalysisResult]:
        logger.info(f"Analyzing review: {review_text[:50]}...")

        await self._load_models_if_needed()

        # Predict aspect using the new multiclassification model
        predicted_aspect = None
        if self._aspect_model:
            try:
                predictions = await run_in_threadpool(self._aspect_model.predict, [review_text])
                if predictions is not None and len(predictions) > 0:
                    predicted_aspect = str(predictions[0])
            except Exception as e:
                logger.error(f"Aspect inference failed: {str(e)}")
        
        # print("predicted_aspect", predicted_aspect)

        # Fallback to keywords if aspect model prediction fails
        if not predicted_aspect:
            text_lower = review_text.lower()
            for aspect, keywords in self._aspect_keywords.items():
                if any(kw in text_lower for kw in keywords):
                    predicted_aspect = aspect
                    break
            if not predicted_aspect:
                predicted_aspect = "product"

        # Predict sentiment using the old sentiment model
        sentiment = "Neutral"
        if self._sentiment_model:
            try:
                predictions = await run_in_threadpool(self._sentiment_model.predict, [review_text])
                sentiment = str(predictions[0]).capitalize()
            except Exception as e:
                logger.error(f"Sentiment inference failed: {str(e)}")
        # print("sentiment", sentiment)
        # Map result to AnalysisResult object
        return [AnalysisResult(aspect=predicted_aspect, sentiment=sentiment)]


analysis_service = AnalysisService()
