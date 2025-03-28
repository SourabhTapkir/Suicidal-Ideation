from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# Sample tweets data extracted from your dataset
tweets = [
    "my life is meaningless i just want to end my life so badly my life is completely empty and i dont want to have to create meaning in it creating meaning is pain how long will i hold back the urge to run my car head first into the next person coming the opposite way when will i stop feeling jealous of tragic characters like gomer pile for the swift end they were able to bring to their lives",
    "muttering i wanna die to myself daily for a few months now i feel worthless shes my soulmate i cant live in this horrible world without her i am so lonely i wish i could just turn off the part of my brain that feels",
    "work slave i really feel like my only purpose in life is to make a higher man money parents forcing me through college and i have too much on my plate i owe a lot of money i know this is the easy way out but i am really tired all of these issues are on top of dealing with tensions in america as well i want to rest",
    "i did something on the 2 of october i overdosed i just felt so alone and horrible i was in hospital for two days now when i walk down the hallways of my school they always look at me weird and say i should take more pills and i hate it i have no one i have this voice in my head now and it wont go away and i cant be myself anymore thanks for reading",
    "i feel like no one cares i just want to die maybe then i d feel less lonely",
]

# Initialize and fit tokenizer
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(tweets)

# Save the tokenizer as tokenizer.pkl
tokenizer_path = "tokenizer.pkl"
with open(tokenizer_path, "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Tokenizer saved as {tokenizer_path}")
