import uuid
from datetime import datetime
from pydantic import BaseModel


class ContentGenerateRequest(BaseModel):
    topic: str
    target_audience: str
    awareness_level: str
    platform: str
    objective: str
    offer_id: uuid.UUID | None = None


class ContentGenerateResponse(BaseModel):
    topic: str
    audience: str
    awareness_level: str
    platform: str
    objective: str
    generated_content: str
    variation_1: str
    variation_2: str
    framework_used: str
    triggers_used: list[str]
    offer_id: uuid.UUID | None = None


class ContentRead(BaseModel):
    id: uuid.UUID
    topic: str
    platform: str
    generated_content: str
    created_at: datetime
