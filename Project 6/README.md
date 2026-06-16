# Multilingual RAG Chatbot Project

## Overview

This project is a Multilingual AI Chatbot capable of understanding and responding in multiple languages while maintaining conversation context and continuity across language switches.

The system uses Retrieval-Augmented Generation (RAG) with local LLM support and vector-based document retrieval to answer questions from uploaded PDF documents in a conversational manner.

It automatically detects the user’s language, translates queries if needed, retrieves relevant context from stored documents, and generates responses in the same language.

## Internship Task

### Problem Statement

Develop a multilingual chatbot that can understand user queries in different languages and provide accurate, context-aware responses using retrieved document knowledge.

### Expected Outcome

A chatbot that supports multilingual input, retrieves relevant PDF-based information, and responds naturally in the same language as the user.

## Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- Deep Translator
- LangDetect

## Project Structure

```plaintext
Project-6/
│
├── app.py
├── chatbot.py
├── translator.py
├── vector_store.py
├── chat_test.py
├── requirements.txt
├── README.md
│
└── data/
    └── sample.pdf
Requirements
streamlit
langchain
chromadb
ollama
deep-translator
langdetect
Methodology
1. User Input Collection

The user enters a question in any supported language (English, Malayalam, Hindi, Tamil).
The Streamlit interface sends the query to the chatbot system.

2. Language Detection

The system detects the language of the input using LangDetect.
If needed, the query is translated into the model’s working language.

3. Retrieval-Augmented Generation (RAG)

The query is converted into embeddings using Ollama embedding models.
ChromaDB retrieves the most relevant chunks from stored PDF documents.
Relevant context is passed to the LLM for response generation.

4. Response Generation

Ollama LLM generates a contextual response using retrieved data.
The response is translated back into the user’s original language if required.

5. Conversational Memory

The chatbot maintains conversation history for better context retention.
Ensures continuity across multilingual interactions.

Results

The chatbot successfully:

Detects multiple languages automatically
Retrieves relevant information from PDFs
Maintains conversation context
Provides accurate multilingual responses
Works through a simple Streamlit interface
How to Run
Install Dependencies
pip install -r requirements.txt
Run the Application
streamlit run app.py
Sample Workflow
Start the Streamlit application
Upload or load a PDF document
Enter a query in any supported language
The system detects language and processes the query
Relevant information is retrieved from the vector database
The chatbot responds in the same language
Example Queries
Language	User Message
English	What is AI?
Malayalam	AI എന്താണ്?
Hindi	AI क्या है?
Mixed	Explain machine learning in Malayalam
Future Improvements
Voice-based multilingual interaction
More Indian language support
Improved translation accuracy
Faster vector retrieval optimization
Enhanced UI/UX design
Author

Abigail Sara David

Internship Project Submission
