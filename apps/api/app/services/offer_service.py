from sqlmodel import Session, select
from app.db.models import Offer, User
from app.schemas.offers import OfferCreate
from app.services.ai.registry import get_provider


async def create_offer(session: Session, user: User, payload: OfferCreate) -> Offer:
    generated = await get_provider().generate_offer(payload)
    item = Offer(
        user_id=user.id,
        dream_outcome=payload.dream_outcome,
        timeframe=payload.timeframe,
        objection=payload.main_objection,
        proof=payload.proof_elements,
        bonuses=payload.bonuses,
        generated_offer=generated,
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def list_offers(session: Session, user: User):
    return session.exec(select(Offer).where(Offer.user_id == user.id)).all()
