def build_offer_prompt(payload) -> str:
    return f"Create offer: Get {payload.dream_outcome} in {payload.timeframe} without {payload.main_objection}"
