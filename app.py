rom flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from e-bot7!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
