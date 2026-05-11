from pydantic import BaseModel, Field
from typing import List

class ReviewRequest(BaseModel):
    review_text: str = Field(..., description="The product review text to analyze")

class AnalysisResult(BaseModel):
    aspect: str = Field(..., description="The extracted aspect of the product")
    sentiment: str = Field(..., description="The sentiment associated with the aspect (Positive/Negative/Neutral)")

class ReviewResponse(BaseModel):
    review_text: str
    analysis: List[AnalysisResult]
