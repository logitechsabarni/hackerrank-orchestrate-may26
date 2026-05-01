import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_justification(text, product_area, risk, escalated):
    reason = []

    if any(word in text for word in ["fraud", "charged", "unauthorized"]):
        reason.append("Detected financial risk keywords")

    reason.append(f"Mapped to product area: {product_area}")
    reason.append(f"Risk level: {risk['level']}")

    if escalated:
        reason.append("Escalation triggered due to high risk")
    else:
        reason.append("Safe to respond using retrieved documents")

    return " | ".join(reason)
