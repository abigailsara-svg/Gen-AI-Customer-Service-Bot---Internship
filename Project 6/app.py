import streamlit as st
from chatbot import multilingual_chat

# Page settings
st.set_page_config(
    page_title="Multilingual AI Chatbot",
    page_icon="🌍"
)

# Title
st.title("🌍 Multilingual AI Chatbot")

st.write(
    "Ask questions in English, Malayalam, Hindi, or Tamil."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input(
    "Type your message..."
)

# Process input
if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    response = multilingual_chat(user_input)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# Display messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
