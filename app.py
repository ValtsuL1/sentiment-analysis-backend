from flask import Flask, request
from flask_cors import CORS, cross_origin
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def hello_world():
    return "<p>Hello world!!!</p>"

# Post request that gets text from request,
# analyzes it and returns the result
@app.route('/sentiment', methods = ['POST'])
@cross_origin()
def get_sentiment():
    req = request.json
    result = analyzer.polarity_scores(req['text'])
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=False)