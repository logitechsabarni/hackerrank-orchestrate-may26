def classify_request(text):
    text = text.lower()

    if any(x in text for x in ["feature", "add", "improve", "suggest"]):
        return "feature_request"
    elif any(x in text for x in ["error", "bug", "not working", "failed", "issue"]):
        return "bug"
    elif len(text.strip()) < 5 or "hello" in text:
        return "invalid"
    return "product_issue"


def classify_product(text, company):
    text = text.lower()
    company = str(company).lower()

    # Visa
    if any(x in text for x in ["card", "payment", "transaction", "charged", "refund"]):
        return "Payments / Transactions"

    # Authentication
    if any(x in text for x in ["login", "password", "account", "access"]):
        return "Authentication"

    # Claude
    if any(x in text for x in ["api", "model", "token", "rate limit"]):
        return "API / Model Usage"

    # HackerRank
    if any(x in text for x in ["test", "submission", "coding", "challenge"]):
        return "Assessments / Coding"

    if "visa" in company:
        return "Payments / Transactions"
    if "claude" in company:
        return "API / Model Usage"
    if "hackerrank" in company:
        return "Assessments / Coding"

    return "General"
