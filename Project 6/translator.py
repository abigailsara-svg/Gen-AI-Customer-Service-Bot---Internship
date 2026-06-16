from langdetect import detect
from deep_translator import GoogleTranslator

# Detect language
def detect_language(text):

    text_lower = text.lower()

    # Manual language checks
    if "malayalam" in text_lower or "മലയാള" in text_lower:
        return "ml"

    if "hindi" in text_lower:
        return "hi"

    if "tamil" in text_lower:
        return "ta"

    try:
        language = detect(text)
        return language

    except:
        return "en"

# Translate user query to English
def translate_to_english(text, source_lang):

    if source_lang == "en":
        return text

    translated = GoogleTranslator(
        source=source_lang,
        target="en"
    ).translate(text)

    return translated

# Translate chatbot response back
def translate_response(text, target_lang):

    if target_lang == "en":
        return text

    translated = GoogleTranslator(
        source="en",
        target=target_lang
    ).translate(text)

    return translated
