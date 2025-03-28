from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow CORS for frontend-backend interaction

# Load the trained LSTM model
model = load_model('lstm_twitter_model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Preprocessing function
def preprocess_tweet(tweet):
    sequences = tokenizer.texts_to_sequences([tweet])  # Convert text to sequences
    padded = pad_sequences(sequences, maxlen=1000, padding='post', truncating='post')  # Pad to model's input size
    return padded

# Routes
@app.route('/')
def home():
    return render_template('index.html')  # Render the main page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input JSON from the frontend
        data = request.get_json()
        tweet = data.get('tweet', '')

        if not tweet:
            return jsonify({'error': 'No tweet provided'}), 400

        # Preprocess the tweet
        processed_tweet = preprocess_tweet(tweet)

        # Get model prediction
        prediction = model.predict(processed_tweet)
        result = 'Suicidal Ideation' if prediction[0] > 0.5 else 'Not Suicidal'

        return jsonify({'prediction': result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')  # Render the recommendations page

if __name__ == '__main__':
    app.run(debug=True)
