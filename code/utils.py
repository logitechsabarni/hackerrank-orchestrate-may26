import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_justification(text, product_area, risk, escalated):
    reasons = []

    if any(x in text for x in ["fraud", "charged", "unauthorized"]):
        reasons.append("Detected financial/security keywords")

    reasons.append(f"Product area: {product_area}")
    reasons.append(f"Risk: {risk['level']}")

    if escalated:
        reasons.append("Escalated due to high risk")
    else:
        reasons.append("Used corpus retrieval for response")

    return " | ".join(reasons)
