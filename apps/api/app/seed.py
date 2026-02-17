import asyncio
from sqlmodel import Session
from app.db.session import engine
from app.db.models import User
from app.core.security import hash_password
from app.schemas.offers import OfferCreate
from app.schemas.content import ContentGenerateRequest
from app.services.offer_service import create_offer
from app.services.content_service import generate_preview, save_content


async def run_seed():
    with Session(engine) as session:
        user = User(email='demo@forgeai.dev', hashed_password=hash_password('password123'))
        session.add(user)
        session.commit()
        session.refresh(user)
        offer = await create_offer(session, user, OfferCreate(dream_outcome='consistent inbound leads', timeframe='14 days', main_objection='posting daily', proof_elements='3 case studies', bonuses='Hook vault,CTA bank,Checklist'))
        for topic, platform in [('AI lead generation', 'LinkedIn'), ('Offer positioning', 'X')]:
            preview = await generate_preview(ContentGenerateRequest(topic=topic, target_audience='founders', awareness_level='Problem-aware', platform=platform, objective='Growth', offer_id=offer.id))
            await save_content(session, user, preview)


if __name__ == '__main__':
    asyncio.run(run_seed())
