from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

DATA_FOLDER = "data"
DB_FOLDER = "vector_db"

embedding = OllamaEmbeddings(model="llama3")

def update_database():

    documents = []

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(
                os.path.join(DATA_FOLDER, file)
            )

            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_FOLDER
    )

    print("Knowledge base updated successfully.")

if __name__ == "__main__":
    update_database()