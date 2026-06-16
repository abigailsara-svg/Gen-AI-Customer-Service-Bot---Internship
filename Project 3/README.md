# Medical Q&A Chatbot using MedQuAD Dataset

## Overview

This project implements a Medical Question & Answer Chatbot that can answer medical-related queries using the MedQuAD dataset.

The system uses Sentence Transformers, cosine similarity, spaCy, and Streamlit to create a retrieval-based chatbot that provides relevant answers from a medical knowledge base and performs basic medical entity recognition.

## Internship Task

### Problem Statement

Develop a specialized medical question-answering chatbot using the MedQuAD dataset. Implement a retrieval mechanism to find relevant answers, perform basic medical entity recognition (such as symptoms, diseases, and treatments), and create a simple user interface using Streamlit.

### Expected Outcome

A medical chatbot capable of answering user questions by retrieving relevant information from the MedQuAD dataset while identifying basic medical entities from user queries.

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Sentence Transformers
* spaCy

## Project Structure

```text
Project-3/
│
├── MedQuAD/
│
├── data/
│   └── medquad.csv
│
├── app.py
├── chatbot.py
├── entity_recognition.py
├── prepare_data.py
├── requirements.txt
└── README.md
```

## Methodology

### 1. Dataset Preparation

* The MedQuAD dataset is downloaded from GitHub.
* XML files are processed using Python.
* Questions and answers are extracted and converted into CSV format.
* The processed dataset is stored as `medquad.csv`.

### 2. Retrieval-Based Question Answering

* Medical questions from the dataset are converted into embeddings using Sentence Transformers.
* User queries are converted into embeddings.
* Cosine similarity is used to compare the user query with stored questions.
* The most relevant answer is retrieved and displayed.

### 3. Medical Entity Recognition

* Basic medical entities are identified using spaCy and keyword matching.
* The system detects:

  * Symptoms
  * Diseases
  * Treatments

### 4. User Interface

* A Streamlit web application provides an interactive interface.
* Users can enter medical questions.
* The chatbot displays the retrieved answer and detected medical entities.

## Results

The chatbot successfully:

* Answers medical questions using the MedQuAD dataset.
* Retrieves relevant answers using semantic similarity.
* Detects basic medical entities from user queries.
* Provides responses through a Streamlit web interface.
* Processes over 16,000 medical question-answer pairs.

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### Run the Application

```bash
streamlit run app.py
```

## Sample Workflow

1. Launch the Streamlit application.
2. Enter a medical question.
3. The chatbot retrieves the most relevant answer.
4. Medical entities are identified from the query.
5. The answer and detected entities are displayed to the user.

## Sample Questions

* What causes diabetes?
* Symptoms of asthma
* Treatment for fever
* What is lung cancer?

## Future Improvements

* Advanced medical entity recognition.
* Support for larger medical datasets.
* Chat history functionality.
* Voice-based interaction.
* Multiple answer suggestions.
* Confidence score for retrieved answers.

## Disclaimer

This chatbot is developed for educational purposes only and should not be considered professional medical advice.

## Author

Abigail Sara David

Internship Project Submission
