from sentence_transformers import SentenceTransformer

# Load model once when the app starts
labse = SentenceTransformer("sentence-transformers/LaBSE")

def encode_text(text: str):
    embedding = labse.encode(text)
    return embedding.tolist()  # Convert to JSON-serializable
