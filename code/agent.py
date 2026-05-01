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
        issue = str(row.get("issue", ""))
        subject = str(row.get("subject", ""))
        company = str(row.get("company", ""))

        text = preprocess(subject + " " + issue)

        request_type = classify_request(text)
        product_area = classify_product(text, company)

        risk = assess_risk(text)

        # 🚨 ESCALATION
        if risk["level"] == "high":
            return {
                "issue": issue,
                "subject": subject,
                "company": company,
                "response": "This issue may involve sensitive or high-risk information. Please contact official support immediately for assistance.",
                "product_area": product_area,
                "status": "escalated",
                "request_type": request_type,
                "justification": build_justification(text, product_area, risk, True)
            }

        # 🔍 RETRIEVAL
        docs = self.retriever.retrieve(text)
        response = generate_response(docs, text)

        return {
            "issue": issue,
            "subject": subject,
            "company": company,
            "response": response,
            "product_area": product_area,
            "status": "replied",
            "request_type": request_type,
            "justification": build_justification(text, product_area, risk, False)
        }

    def run(self, input_path, output_path):
        df = pd.read_csv(input_path)

        results = []
        for _, row in df.iterrows():
            results.append(self.process_ticket(row))

        pd.DataFrame(results).to_csv(output_path, index=False)
