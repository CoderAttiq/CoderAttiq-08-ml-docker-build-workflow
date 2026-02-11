import pandas as pd

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna()
    return df
