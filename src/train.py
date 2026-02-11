from src.preprocess import load_and_clean_data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train():
    df = load_and_clean_data("data/sample.csv")

    X = df[["age", "income"]]
    y = df["label"]

    model = LogisticRegression()
    model.fit(X, y)

    preds = model.predict(X)
    acc = accuracy_score(y, preds)

    print(f"Training accuracy: {acc}")

if __name__ == "__main__":
    train()
