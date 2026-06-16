# Dynamic Knowledge Base Chatbot Project

## Overview
This project implements a chatbot capable of dynamically expanding its knowledge base by periodically updating a vector database with new information from PDF documents.

The system uses LangChain, ChromaDB, Ollama Embeddings, and Streamlit to create a Retrieval-Augmented Generation (RAG) chatbot that can answer questions based on uploaded documents.

## Internship Task

### Problem Statement
Implement a system for dynamically expanding the chatbot's knowledge base. Create a mechanism to periodically update the vector database with new information from specified sources.

### Expected Outcome
A chatbot that can automatically incorporate new information into its responses over time.

## Technologies Used

- Python
- LangChain
- ChromaDB
- Ollama
- Streamlit

## Project Structure

```
Project-1/
│
├── data/
│   └── Practicum 1.pdf
│
├── vector_db/
│
├── updater.py
├── chatbot.py
├── app.py
└── requirements.txt
```

## Methodology

### 1. Knowledge Base Creation
- PDF documents are stored inside the `data` folder.
- `updater.py` loads PDF files using PyPDFLoader.
- Documents are split into chunks using RecursiveCharacterTextSplitter.
- Embeddings are generated using Ollama.
- Chunks are stored in ChromaDB.

### 2. Dynamic Knowledge Base Update
Whenever a new PDF is added to the `data` folder:

1. Run `updater.py`
2. The vector database is updated automatically.
3. The chatbot gains access to the new information.

### 3. Question Answering
- User enters a query through the Streamlit interface.
- Relevant document chunks are retrieved from ChromaDB.
- Results are displayed to the user.

## Results

The chatbot successfully:
- Reads PDF documents.
- Stores knowledge in a vector database.
- Retrieves relevant information.
- Updates its knowledge base when new PDFs are added.
- Provides document-based responses through a web interface.

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Update Knowledge Base

```bash
python updater.py
```

### Run Chatbot

```bash
streamlit run app.py
```

## Sample Workflow

1. Add a PDF to the `data` folder.
2. Run `updater.py`.
3. Start the Streamlit application.
4. Ask questions related to the PDF.
5. Add another PDF and rerun `updater.py`.
6. The chatbot now answers using information from both PDFs.

## Future Improvements

- Automatic scheduled updates.
- Multiple document format support.
- Better semantic search.
- Integration with larger language models.
- Response generation using retrieved context.

## Author

Abigail Sara David

Internship Project Submission
