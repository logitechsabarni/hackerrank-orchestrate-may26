import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, data_path="../data"):
        self.documents = []
        self.load_data(data_path)

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    def load_data(self, path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        self.documents.append(f.read())

    def retrieve(self, query, k=3):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_vectors)[0]

        top_indices = scores.argsort()[-k:][::-1]
        return [self.documents[i] for i in top_indices]
