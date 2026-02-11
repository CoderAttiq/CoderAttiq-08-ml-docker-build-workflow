from src.preprocess import load_and_clean_data

def test_preprocess():
    df = load_and_clean_data("data/sample.csv")
    assert not df.empty
    assert df.isnull().sum().sum() == 0
