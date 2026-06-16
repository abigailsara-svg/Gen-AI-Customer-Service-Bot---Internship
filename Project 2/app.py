from flask import Flask, render_template, request
import os

from models.vision_model import generate_caption

from reasoning.decision_engine import reason_answer
from reasoning.validator import validate_response

from memory.conversation_memory import (
    save_conversation,
    get_last_conversation
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

last_caption = ""

@app.route("/", methods=["GET", "POST"])
def home():

    global last_caption

    response = ""

    if request.method == "POST":

        user_text = request.form.get("text")

        image = request.files.get("image")

        # If image uploaded
        if image and image.filename != "":

            image_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                image.filename
            )

            image.save(image_path)

            # Generate AI caption
            caption = generate_caption(image_path)

            # Save latest caption
            last_caption = caption

            # Generate intelligent response
            response = validate_response(
                reason_answer(
                    user_text,
                    caption
                )
            )

        # If no image uploaded → use memory
        else:

            if last_caption:

                response = validate_response(
                    reason_answer(
                        user_text,
                        last_caption
                    )
                )

            else:

                response = "No previous image context found."

        # Save conversation history
        save_conversation(
            user_text,
            response
        )

    return render_template(
        "index.html",
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)