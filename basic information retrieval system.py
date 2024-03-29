from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InformationRetrievalSystem:
    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer()

    def preprocess_documents(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def query(self, query_text, num_results=5):
        query_vector = self.vectorizer.transform([query_text])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        document_scores = [(i, score) for i, score in enumerate(cosine_similarities)]
        ranked_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)[:num_results]
        return [(self.documents[i], score) for i, score in ranked_documents]

# Example usage
documents = [
    "The sky is blue.",
    "The sun is bright.",
    "The sun in the sky is bright.",
    "We can see the shining sun, the bright sun.",
    "We see the shining sun."
]

ir_system = InformationRetrievalSystem(documents)
ir_system.preprocess_documents()

query_text = "sun in the sky"
results = ir_system.query(query_text)

print("Query:", query_text)
for document, score in results:
    print("Document:", document)
    print("Score:", score)
    print()
