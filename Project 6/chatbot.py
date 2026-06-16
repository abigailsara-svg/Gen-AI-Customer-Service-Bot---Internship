from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import Chroma

from translator import (
    detect_language,
    translate_to_english,
    translate_response
)

# Embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Load vector database
db = Chroma(
    persist_directory="./db",
    embedding_function=embeddings
)

# Retriever
retriever = db.as_retriever()

# Ollama model
llm = ChatOllama(
    model="llama3"
)

# Chat history
chat_history = []

# Main chatbot function
def multilingual_chat(query):

    global chat_history

    # Detect language
    language = detect_language(query)

    print("Detected Language:", language)

    # Translate to English
    english_query = translate_to_english(
        query,
        language
    )

    print("English Query:", english_query)

    # Retrieve relevant documents
    docs = retriever.invoke(
        english_query
    )

    # Combine document contents
    context = "\n".join([
        doc.page_content for doc in docs
    ])

    # Previous conversation history
    history_text = "\n".join(chat_history)

    # Final prompt
    prompt = f"""
You are a multilingual AI assistant.

Previous Conversation:
{history_text}

Context:
{context}

User Question:
{english_query}

Answer clearly and conversationally.
"""

    # Generate response
    response = llm.invoke(prompt)

    english_response = response.content

    print("English Response:", english_response)

    # Save conversation
    chat_history.append(
        f"User: {english_query}"
    )

    chat_history.append(
        f"Assistant: {english_response}"
    )

    # Translate response back
    final_response = translate_response(
        english_response,
        language
    )

    return final_response
