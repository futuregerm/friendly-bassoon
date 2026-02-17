import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.deps import get_current_user
from app.db.models import User, Content
from app.db.session import get_session
from app.schemas.content import ContentGenerateRequest
from app.services.content_service import generate_preview, save_content, list_content

router = APIRouter(prefix='/content', tags=['content'])


@router.post('/generate')
async def generate(payload: ContentGenerateRequest, user: User = Depends(get_current_user)):
    return await generate_preview(payload)


@router.post('/')
async def save(payload: dict, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    from app.schemas.content import ContentGenerateResponse
    generated = ContentGenerateResponse(**payload)
    return await save_content(session, user, generated)


@router.get('/')
def list_all(platform: str | None = None, skip: int = 0, limit: int = 20, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return {'items': list_content(session, user, platform, skip, limit), 'skip': skip, 'limit': limit}


@router.get('/{content_id}')
def get_one(content_id: uuid.UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    item = session.get(Content, content_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail='Not found')
    return item


@router.delete('/{content_id}')
def delete_one(content_id: uuid.UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    item = session.get(Content, content_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail='Not found')
    session.delete(item)
    session.commit()
    return {'ok': True}


@router.post('/{content_id}/regenerate')
async def regenerate(content_id: uuid.UUID, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    item = session.get(Content, content_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail='Not found')
    payload = ContentGenerateRequest(topic=item.topic, target_audience=item.audience, awareness_level=item.awareness_level, platform=item.platform, objective=item.objective, offer_id=item.offer_id)
    generated = await generate_preview(payload)
    item.variation_1 = generated.variation_1
    item.variation_2 = generated.variation_2
    session.add(item)
    session.commit()
    return item
