from flask import Flask, render_template, request
from model import predict_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        email_text = request.form["email"]

        result = predict_email(email_text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)