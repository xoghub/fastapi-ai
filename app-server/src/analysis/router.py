from typing import Annotated
from fastapi import APIRouter, Depends, status
from src.analysis.schemas import ReviewRequest, ReviewResponse
from src.analysis.service import AnalysisService, analysis_service

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.post(
    "",
    response_model=ReviewResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze product review",
    description="Extract aspects and sentiments from a product review text."
)
async def analyze_review(
    request: ReviewRequest,
    service: Annotated[AnalysisService, Depends(lambda: analysis_service)]
) -> ReviewResponse:
    results = await service.analyze_review(request.review_text)
    return ReviewResponse(
        review_text=request.review_text,
        analysis=results
    )
