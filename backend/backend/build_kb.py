from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    "security_book"
)

with open(
    "knowledge/book.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

chunks = text.split("\n\n")

for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk).tolist()

    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[str(i)]
    )

print("knowledge base built")