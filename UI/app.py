from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app = Flask(__name__)

# Load your LSTM model and tokenizer
model = load_model('D:/Sourabh/sourabh ui/Sourabh/sw-detection/lstm_twitter_model.h5')
with open('D:/Sourabh/sourabh ui/Sourabh/UI/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

MAX_SEQUENCE_LENGTH = 100  # Ensure this matches the input size used during training

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'tweet' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    tweet = data['tweet']
    sequence = tokenizer.texts_to_sequences([tweet])
    padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)

    prediction = model.predict(padded_sequence)
    result = "Suicidal Ideation" if prediction[0][0] > 0.5 else "Non-Suicidal"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
