import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from deep_translator import GoogleTranslator

# Load dataset
data = pd.read_csv("dataset.csv")

X = data["description"]
y = data["mudra"]

# -----------------------------
# Improved Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2)
)

X_vec = vectorizer.fit_transform(X)

# -----------------------------
# Model Training
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# -----------------------------
# Translation
# -----------------------------
def translate_to_english(text):
    try:
        return GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)
    except:
        return text

# -----------------------------
# Prediction Function
# -----------------------------
def predict_mudra(text):
    text = translate_to_english(text)
    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]
    return prediction