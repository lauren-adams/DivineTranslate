from flask import Flask

app = Flask(__name__)


@app.route("/members")
def members():
    return{"members":["Member1","Mem2", "test"]}

if __name__ == "__main__":
    app.run(debug=True)