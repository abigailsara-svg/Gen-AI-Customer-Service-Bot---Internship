# Multi-Modal AI Assistant

An advanced AI assistant capable of understanding both text and image inputs using Computer Vision and NLP techniques.

## Features

- Multi-modal AI interaction
- Image understanding using BLIP model
- Conversational memory
- Context awareness
- Contextual reasoning engine
- Response validation
- Ambiguity handling
- Follow-up question support

## Technologies Used

- Python
- Flask
- Transformers
- PyTorch
- BLIP Image Captioning Model
- HTML/CSS

## Project Structure
bash
Project-2/
├── app.py
├── requirements.txt
├── README.md
├── memory/
│   └── conversation_memory.py
├── reasoning/
│   ├── decision_engine.py
│   └── validator.py
├── models/
│   └── vision_model.py
├── templates/
│   └── index.html
├── uploads/
├── static/
└── venv/


## Installation

1. Clone repository

git clone <repository-link>

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

Windows:

.\venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

5. Run project

python app.py

Open browser:

http://127.0.0.1:5000

## Example Usage

- Upload an image
- Ask questions like:
  - What animal is this?
  - What color is it?
  - What is happening in the image?
  - Where is the object located?

The AI assistant remembers previous context and answers intelligently.

## Internship Task Objectives Achieved

- Multi-modal understanding
- Contextual reasoning
- Conversational memory
- Intelligent decision-making
- Evidence-based responses
- Validation handling

## Future Enhancements

- Voice interaction support
- Real-time webcam analysis
- Database-based long-term memory
- Advanced NLP reasoning
- Cloud deployment support

## Author

Abigail Sara David
