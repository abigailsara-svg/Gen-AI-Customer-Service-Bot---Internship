import streamlit as st
from chatbot import get_answer
from entity_recognition import detect_entities

st.title("Medical Q&A Chatbot")

st.warning("This chatbot is for educational purposes only and not medical advice.")

question = st.text_input("Ask a medical question")

if st.button("Get Answer"):

    if question:

        answer = get_answer(question)

        entities = detect_entities(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Detected Medical Entities")
        st.json(entities)