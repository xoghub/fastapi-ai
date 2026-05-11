import logging
import os
from typing import List
import joblib
from fastapi.concurrency import run_in_threadpool
from src.analysis.schemas import AnalysisResult

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self._model = None
        # Path to model relative to project root
        self._model_path = os.path.normpath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "..",
                "artifacts",
                "model",
                "svm_absa_pipeline_2026-05-08.pkl",
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

    async def _get_model(self):
        """Lazily load the model in a threadpool to avoid blocking the event loop."""
        if self._model is None:
            if not os.path.exists(self._model_path):
                logger.error(f"Model file not found at {self._model_path}")
                return None

            try:
                logger.info(f"Loading ML model from {self._model_path}...")
                self._model = await run_in_threadpool(joblib.load, self._model_path)
                logger.info("Model loaded successfully.")
            except Exception as e:
                logger.error(f"Failed to load model: {str(e)}")
                return None
        return self._model

    async def analyze_review(self, review_text: str) -> List[AnalysisResult]:
        logger.info(f"Analyzing review: {review_text[:50]}...")

        model = await self._get_model()

        # Identify aspects based on keywords
        text_lower = review_text.lower()
        found_aspects = []
        for aspect, keywords in self._aspect_keywords.items():
            if any(kw in text_lower for kw in keywords):
                found_aspects.append(aspect)

        # Default to "product" if no specific aspect found
        if not found_aspects:
            found_aspects.append("product")

        # Predict sentiment using the model in a threadpool (CPU intensive)
        sentiment = "Neutral"
        if model:
            try:
                # model.predict expects a sequence of texts
                predictions = await run_in_threadpool(model.predict, [review_text])
                print(predictions)
                # predictions[0] is likely 'positive', 'negative', or 'neutral'
                sentiment = str(predictions[0]).capitalize()
            except Exception as e:
                logger.error(f"Inference failed: {str(e)}")

        # Map results to AnalysisResult objects
        return [
            AnalysisResult(aspect=aspect, sentiment=sentiment)
            for aspect in found_aspects
        ]


analysis_service = AnalysisService()
