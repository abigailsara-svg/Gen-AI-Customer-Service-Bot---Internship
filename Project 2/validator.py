def validate_response(response):

    if not response:
        return "Unable to generate response."

    if len(response.strip()) == 0:
        return "Empty response generated."

    return response