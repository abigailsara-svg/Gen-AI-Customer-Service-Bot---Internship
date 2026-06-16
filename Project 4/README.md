# AI Research Paper Assistant Project

## Overview

This project implements an AI-powered Research Paper Assistant capable of retrieving scientific papers and generating intelligent explanations for advanced research topics.

The system uses Sentence Transformers, FAISS Vector Database, Ollama, Phi-3 LLM, and Streamlit to create a Retrieval-Augmented Generation (RAG) chatbot that can understand user queries semantically and provide AI-generated research explanations.

---

# Internship Task

## Problem Statement

Develop a chatbot that serves as an expert in a specific domain, capable of answering complex queries and explaining concepts using research papers from the arXiv dataset.

The chatbot should:

* Retrieve relevant research papers
* Generate AI-powered explanations
* Handle advanced research-related questions
* Use open-source LLMs for response generation
* Provide an interactive web interface

---

# Expected Outcome

A chatbot capable of:

* Searching scientific research papers semantically
* Explaining advanced concepts in simple language
* Generating AI-based summaries and insights
* Providing intelligent responses using research context
* Supporting research exploration through an interactive UI

---

# Technologies Used

* Python
* Streamlit
* Sentence Transformers
* FAISS Vector Database
* Ollama
* Phi-3 Open Source LLM
* Pandas
* NumPy
* arXiv Dataset

---

# Project Structure

```bash
Project-4/
│
├── data/
│   └── arxiv_sample.csv
│
├── models/
│   ├── arxiv_index.faiss
│   └── papers.pkl
│
├── app.py
├── chatbot.py
├── data_loader.py
├── embeddings.py
├── requirements.txt
│
└── arxiv-metadata-oai-snapshot.json
```

---

# Methodology

## 1. Dataset Preparation

* Downloaded the arXiv dataset from Kaggle.
* Filtered Computer Science research papers.
* Extracted:

  * Paper titles
  * Abstracts
  * Categories
* Stored cleaned data in CSV format.

---

## 2. Embedding Generation

* Used Sentence Transformers (`all-MiniLM-L6-v2`) to generate semantic embeddings.
* Converted research paper abstracts into vector representations.
* Prepared embeddings for similarity search.

---

## 3. Vector Database Creation

* Implemented FAISS vector indexing for efficient semantic retrieval.
* Stored embeddings and paper metadata inside the vector database.
* Enabled fast similarity-based research paper search.

---

## 4. Semantic Research Retrieval

* User queries are converted into embeddings.
* FAISS retrieves the most relevant research papers.
* Retrieved papers are displayed with:

  * Titles
  * Categories
  * Abstracts

---

## 5. AI Explanation Generation

* Integrated Phi-3 Open Source LLM using Ollama.
* Generated AI-powered explanations from retrieved research papers.
* Responses include:

  * Overview
  * Key Concepts
  * Research Insights
  * Real-World Applications

---

## 6. Streamlit Web Application

Built an interactive web interface using Streamlit with:

* Research question input
* Semantic paper retrieval
* AI-generated explanations
* Sidebar information
* Search history tracking

---

# Results

The AI Research Assistant successfully:

* Retrieves relevant research papers semantically
* Generates AI-powered explanations
* Explains advanced research topics
* Uses Retrieval-Augmented Generation (RAG)
* Provides an interactive research exploration interface
* Handles research-related user queries effectively

---

# How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Dataset

```bash
python data_loader.py
```

---

## Create Embeddings and Vector Database

```bash
python embeddings.py
```

---

## Run Streamlit Application

```bash
streamlit run app.py
```

---

# Sample Workflow

1. User enters a research question.
2. Query is converted into embeddings.
3. FAISS retrieves similar research papers.
4. Phi-3 generates AI explanations.
5. Results are displayed in Streamlit UI.

---

# Future Improvements

* Conversational memory
* PDF export functionality
* Advanced search filters
* Concept visualization
* Online deployment
* Multi-domain research support
* Improved response generation

---

# Author

Abigail Sara David

Internship Project Submission
