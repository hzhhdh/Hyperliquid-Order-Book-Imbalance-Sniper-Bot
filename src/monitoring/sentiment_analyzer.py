async def analyze_sentiment(text: str) -> float:
    sentiment = await run_nlp_model(text)
    return sentiment.score
