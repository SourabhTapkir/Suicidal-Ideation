import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model
model = tf.keras.models.load_model("D:/Sourabh/sourabh ui/Sourabh/sw-detection/lstm_twitter_model.h5")

# Load the tokenizer
with open("tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

MAX_SEQUENCE_LENGTH = 1000  # The sequence length that the model expects

def predict_suicidal_ideation(tweet):
    # Tokenize the input tweet
    sequences = tokenizer.texts_to_sequences([tweet])
    
    # Pad the sequences to ensure consistent input size
    padded_sequence = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
    
    # Get the prediction probabilities from the model
    prediction_probs = model.predict(padded_sequence)
    probability = float(prediction_probs[0][0])
    # Convert the prediction probability to a binary result (1 for suicidal ideation, 0 for not)
    prediction = int(prediction_probs > 0.5)
    
    # Map the prediction to a human-readable result
    result = 'Suicidal Ideation' if prediction == 1 else 'Not Suicidal'
  #  print(f"Prediction: {result} (Probability: {prediction_probs[0]:.4f})")
    print(f"Prediction: {result} (Probability: {probability:.4f})")
if __name__ == "__main__":
    tweet = input("Enter the tweet to predict suicidal ideation: ")
    predict_suicidal_ideation(tweet)
