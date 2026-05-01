import pandas as pd
from classifier import classify_request, classify_product
from risk_engine import assess_risk
from retriever import Retriever
from responder import generate_response
from utils import preprocess, build_justification

class SupportAgent:
    def __init__(self):
        self.retriever = Retriever()

    def process_ticket(self, row):
        text = preprocess(str(row["subject"]) + " " + str(row["issue"]))

        request_type = classify_request(text)
        product_area = classify_product(text)

        risk = assess_risk(text)

        if risk["level"] == "high":
            return {
                "status": "escalated",
                "product_area": product_area,
                "response": "This issue requires human support. Please contact the support team directly for immediate assistance.",
                "justification": build_justification(text, product_area, risk, escalated=True),
                "request_type": request_type
            }

        docs = self.retriever.retrieve(text)
        response = generate_response(docs)

        return {
            "status": "replied",
            "product_area": product_area,
            "response": response,
            "justification": build_justification(text, product_area, risk, escalated=False),
            "request_type": request_type
        }

    def run(self, input_path, output_path):
        df = pd.read_csv(input_path)

        results = []
        for _, row in df.iterrows():
            result = self.process_ticket(row)
            results.append(result)

        pd.DataFrame(results).to_csv(output_path, index=False)
