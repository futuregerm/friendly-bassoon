from typing import Protocol
from app.schemas.content import ContentGenerateRequest, ContentGenerateResponse
from app.schemas.offers import OfferCreate


class AIProvider(Protocol):
    async def generate_content(self, payload: ContentGenerateRequest) -> ContentGenerateResponse: ...
    async def generate_offer(self, payload: OfferCreate) -> str: ...
