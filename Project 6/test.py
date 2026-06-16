from translator import (
    detect_language,
    translate_to_english
)

text = "മെഷീൻ ലേണിംഗ് എന്താണ്?"

lang = detect_language(text)

print("Detected Language:", lang)

translated = translate_to_english(
    text,
    lang
)

print("Translated:", translated)
