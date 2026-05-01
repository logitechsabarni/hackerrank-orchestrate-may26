def generate_response(docs):
    if not docs:
        return "Sorry, we could not find relevant information. Please contact support."

    # simple safe summarization
    return docs[0][:300]
