import hashlib
from app.schemas.content import ContentGenerateRequest, ContentGenerateResponse
from app.schemas.offers import OfferCreate


class MockProvider:
    async def generate_content(self, payload: ContentGenerateRequest) -> ContentGenerateResponse:
        seed = hashlib.md5(f"{payload.topic}-{payload.platform}-{payload.awareness_level}-{payload.objective}".encode()).hexdigest()[:8]
        hook = f"Stop scrolling: {payload.topic} is where most {payload.target_audience} lose momentum."
        if payload.platform == "Instagram":
            body = "\n".join(["Slide 1: Hook", "Slide 2-8: Story + steps", "Slide 9: CTA"])
        elif payload.platform == "Email":
            body = "Subject: Quick win for your pipeline\nOpening: Matches subject\nStory\nCTA\nPS urgency"
        elif payload.platform == "YouTube":
            body = "Title\nHook\nOutline\nMid-roll CTAs\nFinal CTA"
        elif payload.platform == "LinkedIn":
            body = "Story-driven post with whitespace and soft CTA to comment/DM"
        else:
            body = "Thread:\n1) Problem\n2) Method\n3) Steps\n4) CTA to follow/repost"
        cta = {
            "Growth": "Save this and share it.",
            "Sales": "Book a call today, risk-free.",
            "Authority": "Comment AUTHORITY for my breakdown.",
            "Lead Gen": "DM LEAD for the playbook."
        }.get(payload.objective, "Follow for more")
        text = f"{hook}\n\n{body}\n\n{cta}"
        return ContentGenerateResponse(
            topic=payload.topic,
            audience=payload.target_audience,
            awareness_level=payload.awareness_level,
            platform=payload.platform,
            objective=payload.objective,
            offer_id=payload.offer_id,
            generated_content=f"[{seed}] {text}",
            variation_1=f"Variation A: {text}",
            variation_2=f"Variation B: {text}",
            framework_used=f"AWARENESS-{payload.awareness_level}",
            triggers_used=["Curiosity", "Specificity", "Urgency"]
        )

    async def generate_offer(self, payload: OfferCreate) -> str:
        bonuses = [x.strip() for x in payload.bonuses.split(',') if x.strip()][:3]
        while len(bonuses) < 3:
            bonuses.append(f"Bonus {len(bonuses)+1}")
        return (
            f"Get {payload.dream_outcome} in {payload.timeframe} without {payload.main_objection}. "
            f"Bonuses: {', '.join(bonuses)}. Guarantee: 14-day action guarantee. Urgency: closes Friday."
        )
