import logging
from typing import List
from src.analysis.schemas import AnalysisResult

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        # In a real scenario, we would load the model here
        pass

    async def analyze_review(self, review_text: str) -> List[AnalysisResult]:
        logger.info(f"Analyzing review: {review_text[:50]}...")
        
        # Mock logic
        mock_results = [
            AnalysisResult(aspect="product", sentiment="Positive")
        ]
        
        text_lower = review_text.lower()
        if "battery" in text_lower:
            mock_results.append(AnalysisResult(aspect="battery", sentiment="Negative"))
        if "screen" in text_lower:
            mock_results.append(AnalysisResult(aspect="screen", sentiment="Positive"))
            
        return mock_results

analysis_service = AnalysisService()
