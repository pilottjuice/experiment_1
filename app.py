from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    status = request.args.get("status")
    return render_template("index.html", status=status)


@app.route("/update", methods=["POST"])
def update_file():

    user_text = request.form["user_text"]

    with open("example.txt", "a", encoding="utf-8") as file:
        file.write("\n" + user_text)

    return redirect(url_for("home", status="Your text is updated!"))


@app.route("/clear", methods=["POST"])
def clear_file():

    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("")

    return redirect(url_for("home", status="The file has been cleared!"))


if __name__ == "__main__":
    app.run(debug=True)