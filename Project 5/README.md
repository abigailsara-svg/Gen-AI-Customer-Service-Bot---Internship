# Sentiment Aware Chatbot Project

## Overview

This project implements a chatbot capable of detecting user emotions from text messages using Natural Language Processing (NLP).

The system uses Python, TextBlob, and Streamlit to classify user messages into Positive, Negative, or Neutral sentiments and generate appropriate responses based on the detected emotion.

## Internship Task

### Problem Statement

Integrate sentiment analysis into the chatbot to detect and respond appropriately to customer emotions during interactions.

### Expected Outcome

A chatbot that can recognize and address positive, negative, or neutral sentiments in user messages.

## Technologies Used

* Python
* Streamlit
* TextBlob
* Natural Language Processing (NLP)

## Project Structure

```plaintext id="e0pc2g"
Project-5/
│
├── app.py
├── sentiment.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Requirements

```plaintext id="x6a3ut"
streamlit
textblob
```

## Methodology

### 1. User Input Collection

* The user enters a message through the Streamlit interface.
* The chatbot receives the text input for analysis.

### 2. Sentiment Analysis

* TextBlob analyzes the polarity of the user message.
* Based on the polarity score:

  * Positive sentiment is detected for happy or satisfied messages.
  * Negative sentiment is detected for sad or dissatisfied messages.
  * Neutral sentiment is detected for normal or informational messages.

### 3. Emotion-Based Response

* The chatbot generates different responses depending on the detected sentiment.
* Responses are designed to improve customer interaction and engagement.

## Results

The chatbot successfully:

* Detects user emotions from text.
* Classifies sentiments into Positive, Negative, and Neutral.
* Responds appropriately based on user emotion.
* Provides a simple and interactive web interface using Streamlit.

## How to Run

### Install Dependencies

```bash id="rkzwwq"
pip install -r requirements.txt
```

### Run the Application

```bash id="ytk1gr"
python -m streamlit run app.py
```

## Sample Workflow

1. Start the Streamlit application.
2. Enter a message into the chatbot.
3. The chatbot analyzes the sentiment of the message.
4. The detected sentiment is displayed.
5. The chatbot provides an emotion-based response.

## Example Outputs

| User Message              | Detected Sentiment |
| ------------------------- | ------------------ |
| "This is amazing!"        | Positive           |
| "I am very disappointed." | Negative           |
| "Can you help me?"        | Neutral            |

## Future Improvements

* Advanced emotion detection
* Voice-based chatbot interaction
* Chat history support
* AI-generated dynamic responses
* Multi-language sentiment analysis

## Author

Abigail Sara David

Internship Project Submission
