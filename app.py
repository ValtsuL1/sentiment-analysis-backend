from flask import Flask, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()

@app.route("/")
def hello_world():
    return "<p>Hello world!!!</p>"

@app.route("/sentiment")
def get_sentiment():
    data = request.json
    print(data)

if __name__ == "__main__":
    app.run()