from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings

DB_FOLDER = "vector_db"

embedding = OllamaEmbeddings(model="llama3")

db = Chroma(
    persist_directory=DB_FOLDER,
    embedding_function=embedding
)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(query, k=3)

    print("\nRetrieved Knowledge:\n")

    for doc in docs:
        print(doc.page_content[:300])
        print("-" * 40)