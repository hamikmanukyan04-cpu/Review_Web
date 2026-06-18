import joblib

model = joblib.load("text_classifier.pkl")

def predict(text):
    return model.predict([text])[0]

print(predict("bitcoin and crypto market is rising"))
print(predict("football match ended with big score"))