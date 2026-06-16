# Multilingual RAG Chatbot Project

## Overview

This project implements a multilingual chatbot capable of understanding and responding in multiple languages while maintaining conversational context across language switches.

The system uses LangChain, ChromaDB, Ollama, LangDetect, Deep Translator, and Streamlit to create a Retrieval-Augmented Generation (RAG) chatbot that supports multilingual conversations and document-based question answering.

## Internship Task

### Problem Statement

Extend the existing chatbot to support multilingual conversations across multiple languages while preserving context, intent, and conversational continuity throughout language switches.

The assistant should automatically identify languages, manage multilingual inputs, retrieve relevant information from documents, and provide responses in the user's language.

### Expected Outcome

A multilingual chatbot capable of:

- Detecting user language automatically.
- Supporting cross-language conversations.
- Maintaining conversation context.
- Retrieving information from PDF documents.
- Generating accurate responses in multiple languages.

---

## Technologies Used

- Python
- LangChain
- ChromaDB
- Ollama
- Streamlit
- LangDetect
- Deep Translator

---

## Project Structure

```text
Project-6/
│
├── sample.pdf
│
├── vector_store.py
├── chatbot.py
├── translator.py
├── chat_test.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Knowledge Base Creation

- PDF documents are loaded using PyPDFLoader.
- Documents are split into smaller chunks.
- Embeddings are generated using Ollama Embeddings.
- Chunks are stored in ChromaDB vector database.

### 2. Language Detection

- User input is analyzed using LangDetect.
- The system automatically identifies the language of the query.
- Supported languages include English, Malayalam, Hindi, and Tamil.

### 3. Translation Pipeline

- Queries are translated to English for processing.
- Retrieved responses are translated back into the user's language.
- Deep Translator is used for multilingual translation.

### 4. Context Retention

- Previous conversations are stored in memory.
- Context is preserved across language switches.
- Users can continue conversations in different languages without losing continuity.

### 5. Question Answering

- User submits a query through the Streamlit interface.
- Relevant document chunks are retrieved from ChromaDB.
- Ollama generates responses using the retrieved context.
- Responses are returned in the user's language.

---

## Results

The chatbot successfully:

- Detects multiple languages automatically.
- Retrieves relevant information from PDF documents.
- Maintains conversational context.
- Supports multilingual conversations.
- Handles language switching during conversations.
- Generates responses in the user's language.
- Works through a Streamlit web interface.

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Vector Database

```bash
python vector_store.py
```

### Run the Application

```bash
streamlit run app.py
```

---

## Sample Workflow

1. Create the vector database using PDF documents.
2. Start the Streamlit application.
3. Enter a query in English, Malayalam, Hindi, or Tamil.
4. The system detects the language automatically.
5. Relevant information is retrieved from the vector database.
6. The chatbot generates a response in the same language.
7. Continue the conversation in another language while maintaining context.

---

## Example Queries

### English

```
What is AI?
```

### Malayalam

```
AI എന്താണ്?
```

### Hindi

```
AI क्या है?
```

### Mixed Language

```
Explain machine learning in Malayalam
```

---

## Future Improvements

- Voice-based multilingual interaction.
- Support for additional languages.
- Improved translation accuracy.
- Enhanced conversational memory.
- Real-time document updates.
- Better user interface design.

---

## Author

Abigail Sara David

Internship Project Submission
