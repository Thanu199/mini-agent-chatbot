from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("data/documents.txt", "r", encoding="utf-8") as f:
    documents = f.read().split("\n\n")

doc_embeddings = model.encode(documents, convert_to_tensor=True)

def search_document(query: str):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, doc_embeddings)[0]
    best_idx = scores.argmax()

    if scores[best_idx] > 0.4:
        return documents[int(best_idx)]
    return None
