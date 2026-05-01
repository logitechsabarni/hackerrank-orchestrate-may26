HIGH_RISK_KEYWORDS = [
    "fraud", "unauthorized", "stolen",
    "charged", "refund", "hacked",
    "suspicious", "unknown transaction"
]

def assess_risk(text):
    text = text.lower()
    score = 0

    for word in HIGH_RISK_KEYWORDS:
        if word in text:
            score += 2

    if score >= 2:
        return {"level": "high", "score": score}
    return {"level": "low", "score": score}
