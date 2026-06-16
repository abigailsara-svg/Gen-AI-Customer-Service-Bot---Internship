conversation_history = []

def save_conversation(user_input, ai_response):

    conversation_history.append({
        "user": user_input,
        "assistant": ai_response
    })

def get_last_conversation():

    if conversation_history:
        return conversation_history[-1]

    return None