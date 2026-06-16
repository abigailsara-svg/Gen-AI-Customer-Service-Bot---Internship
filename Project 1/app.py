import streamlit as st
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embedding = OllamaEmbeddings(model="llama3")

db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

st.title("📚 PDF Chatbot")

query = st.text_input("Ask a question:")

if query:
    docs = db.similarity_search(query, k=3)

    st.write("### Results")

    for doc in docs:
        st.write(doc.page_content)