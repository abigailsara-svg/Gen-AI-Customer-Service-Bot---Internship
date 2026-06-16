import spacy

nlp = spacy.load("en_core_web_sm")

medical_terms = {
    "symptoms": ["fever", "cough", "headache"],
    "diseases": ["diabetes", "cancer", "asthma"],
    "treatments": ["insulin", "chemotherapy"]
}

def detect_entities(text):

    text = text.lower()

    found = {
        "symptoms": [],
        "diseases": [],
        "treatments": []
    }

    for category, words in medical_terms.items():

        for word in words:

            if word in text:
                found[category].append(word)

    return found