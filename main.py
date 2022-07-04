import os
from flask import Flask, request, render_template
from uuid import uuid4 as v4

app = Flask(__name__)
app.template_folder = "templates"


@app.get("/")
def root():
    return render_template("index.html"), 200


@app.post("/upload")
def receive_image():
    try:
        image_file = request.files["file"]
        image_file.save(f"uploads/{v4()}{image_file.filename}")

        return {
            "message": "Successfully uploaded file.",
        }, 200
    except Exception as e:
        print(f"[ERROR] {e}")

        return {
            "error": "Couldn't find file in the request",
        }, 400


if __name__ == "__main__":
    app.run(debug=True)
