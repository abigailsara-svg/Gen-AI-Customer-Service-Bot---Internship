# Medical Q&A Chatbot using MedQuAD Dataset

## Project Overview
This project is a Medical Question & Answer Chatbot developed using the MedQuAD dataset. The chatbot can answer medical-related questions by retrieving the most relevant answer from the dataset. It also performs basic medical entity recognition for symptoms, diseases, and treatments.

## Features
- Medical question answering system
- Retrieval-based chatbot using sentence similarity
- Medical entity recognition
- Streamlit web interface
- Uses MedQuAD medical dataset
- Educational medical assistant

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- Sentence Transformers
- spaCy

## Dataset
MedQuAD Dataset:
https://github.com/abachaa/MedQuAD

## Project Structure

```text
Project-3/
│
├── MedQuAD/
├── data/
│   └── medquad.csv
├── app.py
├── chatbot.py
├── entity_recognition.py
├── prepare_data.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository
```bash
git clone <your-github-repo-link>
cd Project-3
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### 4. Run the Application
```bash
streamlit run app.py
```

## How It Works
1. The MedQuAD XML dataset is converted into CSV format.
2. Questions are converted into embeddings using Sentence Transformers.
3. User questions are compared with dataset questions using cosine similarity.
4. The most relevant medical answer is displayed.
5. Medical entities are detected and shown separately.

## Sample Questions
- What causes diabetes?
- Symptoms of asthma
- Treatment for fever
- What is lung cancer?

## Disclaimer
This chatbot is developed for educational purposes only and should not be considered professional medical advice.

## Author
Abigail Sara David
