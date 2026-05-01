def generate_response(docs, query):
    if not docs:
        return "We could not find relevant information. Please contact support."

    base = docs[0][:400]

    # Light contextual improvement
    if "login" in query:
        return "Try resetting your password or checking your credentials. " + base

    if "payment" in query or "card" in query:
        return "Please verify your transaction details and contact support if needed. " + base

    return base
