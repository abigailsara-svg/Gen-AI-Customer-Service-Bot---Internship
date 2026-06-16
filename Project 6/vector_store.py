from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def create_vector_db():

    # Load PDF
    loader = PyPDFLoader("data/sample.pdf")
    documents = loader.load()

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(documents)

    # Embedding model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Create vector database
    vectorstore = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="./db"
    )

    vectorstore.persist()

    print("Vector Database Created Successfully!")

if __name__ == "__main__":
    create_vector_db()
