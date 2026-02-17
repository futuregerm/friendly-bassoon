from sqlmodel import Session, select
from app.db.models import Content, User
from app.schemas.content import ContentGenerateRequest, ContentGenerateResponse
from app.services.ai.registry import get_provider


async def generate_preview(payload: ContentGenerateRequest) -> ContentGenerateResponse:
    return await get_provider().generate_content(payload)


async def save_content(session: Session, user: User, generated: ContentGenerateResponse) -> Content:
    item = Content(
        user_id=user.id,
        topic=generated.topic,
        audience=generated.audience,
        awareness_level=generated.awareness_level,
        platform=generated.platform,
        objective=generated.objective,
        offer_id=generated.offer_id,
        generated_content=generated.generated_content,
        variation_1=generated.variation_1,
        variation_2=generated.variation_2,
        framework_used=generated.framework_used,
        triggers_used=",".join(generated.triggers_used),
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def list_content(session: Session, user: User, platform: str | None, skip: int, limit: int):
    stmt = select(Content).where(Content.user_id == user.id)
    if platform:
        stmt = stmt.where(Content.platform == platform)
    return session.exec(stmt.offset(skip).limit(limit)).all()
