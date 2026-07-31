from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return Response("Jenkins CI/CD pipeline works!\n This is my v4", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
