def classify_request(text):
    text = text.lower()

    if "feature" in text or "add" in text:
        return "feature_request"
    elif "error" in text or "not working" in text or "failed" in text:
        return "bug"
    elif "hello" in text or len(text.strip()) < 5:
        return "invalid"
    return "product_issue"


def classify_product(text):
    text = text.lower()

    if "card" in text or "transaction" in text or "payment" in text:
        return "Payments / Transactions"
    elif "api" in text or "model" in text or "key" in text:
        return "API / Model Usage"
    elif "test" in text or "submission" in text or "coding" in text:
        return "Assessments / Coding"
    elif "login" in text or "password" in text:
        return "Authentication"
    return "General"
