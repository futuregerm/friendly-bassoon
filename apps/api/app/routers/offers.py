import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.deps import get_current_user
from app.db.models import User, Offer
from app.db.session import get_session
from app.schemas.offers import OfferCreate
from app.services.offer_service import create_offer, list_offers

router = APIRouter(prefix='/offers', tags=['offers'])


@router.post('/')
async def create(payload: OfferCreate, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return await create_offer(session, user, payload)


@router.get('/')
def list_all(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return {'items': list_offers(session, user)}


@router.get('/{offer_id}')
def get_one(offer_id: uuid.UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    item = session.get(Offer, offer_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail='Not found')
    return item


@router.delete('/{offer_id}')
def delete_one(offer_id: uuid.UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    item = session.get(Offer, offer_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail='Not found')
    session.delete(item)
    session.commit()
    return {'ok': True}
