from flask import Flask, request, render_template
from uuid import uuid4 as v4

app = Flask(__name__)
app.template_folder = "templates"


@app.get("/")
def root():
    # Renders the "template/index.html" to a static page
    # to be accessed over "http://localhost:5000/".
    return render_template("index.html"), 200


@app.post("/upload")
def receive_image():
    # Route to receive an image file from the HTTP request.
    try:
        # Gets the image file from the request form
        # and aves it to the uploads folder locally.
        image_file = request.files["file"]
        image_file.save(f"uploads/{v4()}{image_file.filename}")

        # Returns a JSON message indicating that the file
        # was received successfully.
        return {
            "message": "Successfully uploaded file.",
        }, 200
    except Exception as e:
        print(f"[ERROR] {e}")

        return {
            "error": "Couldn't find file in the request",
        }, 400


if __name__ == "__main__":
    # Access http://localhost:5000/ to get the index route.
    app.run(debug=True)
