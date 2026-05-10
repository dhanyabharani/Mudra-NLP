import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from deep_translator import GoogleTranslator

# -----------------------------
# Dataset Path Fix
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "dataset.csv")

# Load dataset
data = pd.read_csv(dataset_path)

# Features & Labels
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
# Translation Function
# -----------------------------
def translate_to_english(text):
    try:
        translated_text = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        return translated_text

    except:
        return text


# -----------------------------
# Prediction Function
# -----------------------------
def predict_mudra(text):

    # Translate input to English
    translated_text = translate_to_english(text)

    # Convert text to vector
    text_vec = vectorizer.transform([translated_text])

    # Predict mudra
    prediction = model.predict(text_vec)[0]

    return prediction
