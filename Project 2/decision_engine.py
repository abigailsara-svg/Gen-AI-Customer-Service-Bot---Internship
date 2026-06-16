def reason_answer(user_question, image_caption):

    question = user_question.lower()

    caption = image_caption.lower()

    # Animal detection
    if "animal" in question or "what is this" in question:

        if "dog" in caption:
            return "The image appears to contain a dog."

        elif "cat" in caption:
            return "The image appears to contain a cat."

        else:
            return f"I detected: {image_caption}"

    # Color reasoning
    elif "color" in question:

        return (
            "The exact color is unclear, "
            "but the object is visible in the image."
        )

    # Location reasoning
    elif "where" in question or "place" in question:

        if "window" in caption:
            return (
                "The image seems to be taken indoors "
                "near a window."
            )

        else:
            return "The exact location is unclear."

    # Contextual reasoning
    elif "doing" in question:

        return (
            f"Based on the image, it appears that: "
            f"{image_caption}"
        )

    # Default intelligent response
    return f"Based on the image, I observe: {image_caption}"