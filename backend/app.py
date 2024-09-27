from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)  # Allow requests from frontend
sia = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    sentiment_score = sia.polarity_scores(text)

    # Determine sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

