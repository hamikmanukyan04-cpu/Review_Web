import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# training data
data = [
    ("I love this product", "positive"),
    ("This is amazing", "positive"),
    ("Very good experience", "positive"),
    ("I am happy with this", "positive"),

    ("I hate this", "negative"),
    ("Worst experience ever", "negative"),
    ("Very bad quality", "negative"),
    ("I am disappointed", "negative"),
]

df = pd.DataFrame(data, columns=["text", "label"])

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(df["text"], df["label"])

joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")