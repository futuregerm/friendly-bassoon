def build_content_prompt(payload) -> str:
    return f"Generate {payload.platform} content for {payload.topic} aimed at {payload.target_audience}. Awareness={payload.awareness_level}. Objective={payload.objective}."
