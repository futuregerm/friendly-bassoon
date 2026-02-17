import uuid
from datetime import datetime
from pydantic import BaseModel


class OfferCreate(BaseModel):
    dream_outcome: str
    timeframe: str
    main_objection: str
    proof_elements: str
    bonuses: str


class OfferRead(BaseModel):
    id: uuid.UUID
    generated_offer: str
    created_at: datetime
