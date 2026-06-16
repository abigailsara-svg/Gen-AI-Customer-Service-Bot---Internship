import streamlit as st
from sentiment import analyze_sentiment

st.title("Sentiment Aware Chatbot")

user_input = st.text_input("Enter your message:")

if user_input:

    sentiment = analyze_sentiment(user_input)

    st.write(f"Detected Sentiment: {sentiment}")

    # Response based on sentiment
    if sentiment == "Positive":
        response = "I'm happy to hear that! 😊"

    elif sentiment == "Negative":
        response = "I'm sorry you're feeling this way. How can I help? 😟"

    else:
        response = "Thank you for sharing. How may I assist you? 🙂"

    st.success(response)