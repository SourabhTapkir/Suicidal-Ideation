import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Step 1: Load the dataset
# Load the tweets and labels
data = pd.read_csv('D:/Sourabh/sourabh ui/Sourabh/sw-detection/data/tweets_dataset.csv')
X_test = data['tweets'].values
y_test = data['y'].values

# Step 2: Preprocess the data
# Tokenize the text data (use the same tokenizer as in model training)
tokenizer = Tokenizer(num_words=10000)  # Update 'num_words' to match your model
tokenizer.fit_on_texts(X_test)  # Only for token consistency; the real tokenizer should match the trained model
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Adjust the 'maxlen' to match the input shape of your model
maxlen = 1000  # Update to the correct sequence length used in your model
X_test_padded = pad_sequences(X_test_seq, maxlen=maxlen)

# Step 3: Load the model
model = load_model('D:/Sourabh/sourabh ui/New folder (2)/lstm_twitter_model.h5')

# Step 4: Make predictions
y_pred_prob = model.predict(X_test_padded)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()

# Step 5: Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Step 6: Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Suicidal', 'Suicidal'], yticklabels=['Not Suicidal', 'Suicidal'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Step 7: Print classification report
print(classification_report(y_test, y_pred, target_names=['Not Suicidal', 'Suicidal']))
