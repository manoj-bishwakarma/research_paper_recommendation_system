import os
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "papers.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "model"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "model.pkl"
)

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "vectorizer.pkl"
)


def train_model():

    print("Loading papers...")

    df = pd.read_csv(DATA_PATH)

    df["text"] = (
        df["title"].fillna("")
        + " "
        + df["keywords"].fillna("")
        + " "
        + df["abstract"].fillna("")
    )

    X = df["text"]

    y = df["category"]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    X_vector = vectorizer.fit_transform(X)

    model = MultinomialNB()

    model.fit(X_vector, y)

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        vectorizer,
        VECTORIZER_PATH
    )

    print("Model trained successfully.")

    print("Classes:")

    print(model.classes_)


if __name__ == "__main__":

    train_model()