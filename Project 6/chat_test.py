from chatbot import multilingual_chat

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    response = multilingual_chat(query)

    print("Bot:", response)
