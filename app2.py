from flask import Flask

app2 = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask CI!"

if __name__ == "__main__":
    app.run()