HIGH_RISK = [
    "fraud", "unauthorized", "stolen", "hacked",
    "charged", "refund", "suspicious",
    "unknown transaction", "money deducted"
]

def assess_risk(text):
    text = text.lower()
    score = 0

    for word in HIGH_RISK:
        if word in text:
            score += 2

    if score >= 2:
        return {"level": "high", "score": score}
    return {"level": "low", "score": score}
