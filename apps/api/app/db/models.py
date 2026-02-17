import uuid
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


def utcnow():
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=utcnow)


class Offer(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id", index=True)
    dream_outcome: str
    timeframe: str
    objection: str
    proof: str
    bonuses: str
    generated_offer: str
    created_at: datetime = Field(default_factory=utcnow)


class Content(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id", index=True)
    topic: str
    audience: str
    awareness_level: str
    platform: str
    objective: str
    offer_id: uuid.UUID | None = Field(default=None, foreign_key="offer.id")
    generated_content: str
    variation_1: str
    variation_2: str
    framework_used: str
    triggers_used: str
    created_at: datetime = Field(default_factory=utcnow)
