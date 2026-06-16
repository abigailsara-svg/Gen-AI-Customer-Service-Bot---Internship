# Multi-Modal AI Assistant

## Overview

This project implements a Multi-Modal AI Assistant capable of understanding both text and image inputs. The assistant combines Computer Vision and Natural Language Processing techniques to analyze images, maintain conversational context, perform reasoning, and generate intelligent responses.

The system uses the BLIP Image Captioning Model, conversational memory, contextual reasoning, and response validation to provide accurate and context-aware interactions.

## Internship Task

### Problem Statement

Develop a Multi-Modal AI Assistant that can process both text and image inputs, maintain conversation context, perform intelligent reasoning, handle ambiguity, and generate meaningful responses through an interactive web interface.

### Expected Outcome

An AI assistant capable of understanding image content, answering user questions, maintaining conversational memory, and providing context-aware responses.

## Technologies Used

* Python
* Flask
* Transformers
* PyTorch
* BLIP Image Captioning Model
* HTML/CSS

## Project Structure

```text
Project-2/
│
├── app.py
├── requirements.txt
├── README.md
│
├── memory/
│   └── conversation_memory.py
│
├── reasoning/
│   ├── decision_engine.py
│   └── validator.py
│
├── models/
│   └── vision_model.py
│
├── templates/
│   └── index.html
│
├── uploads/
├── static/
└── venv/
```

## Methodology

### 1. Image Understanding

* Images are uploaded through the web interface.
* The BLIP Image Captioning Model analyzes image content.
* Relevant descriptions and contextual information are extracted.

### 2. Conversational Memory

* User interactions are stored using a memory module.
* Previous conversations are maintained throughout the session.
* The assistant uses past context to provide better responses.

### 3. Contextual Reasoning

* A decision engine processes user inputs.
* Context from previous interactions is considered.
* Responses are generated based on both image and text information.

### 4. Response Validation

* Generated responses are validated before being displayed.
* Ambiguous queries are identified and handled appropriately.
* Follow-up questions are supported to improve user interaction.

### 5. User Interface

* Flask provides the backend functionality.
* HTML/CSS is used for the frontend interface.
* Users can upload images and ask questions interactively.

## Results

The assistant successfully:

* Understands image content using computer vision.
* Processes text and image inputs together.
* Maintains conversational memory.
* Performs contextual reasoning.
* Handles ambiguous queries.
* Generates intelligent and relevant responses.

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
.\venv\Scripts\Activate.ps1
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

## Sample Workflow

1. Launch the Flask application.
2. Upload an image.
3. Ask a question related to the image.
4. The assistant analyzes the image and query.
5. Contextual reasoning is applied.
6. A validated response is displayed.
7. Continue the conversation using follow-up questions.

## Sample Questions

* What animal is this?
* What color is it?
* What is happening in the image?
* Where is the object located?
* Describe this image.
* What can you infer from this scene?

## Future Improvements

* Voice interaction support.
* Real-time webcam analysis.
* Database-based long-term memory.
* Advanced NLP reasoning.
* Cloud deployment support.
* Multi-language support.

## Internship Task Objectives Achieved

* Multi-modal understanding
* Contextual reasoning
* Conversational memory
* Intelligent decision-making
* Evidence-based responses
* Validation handling

## Author

Abigail Sara David

Internship Project Submission
