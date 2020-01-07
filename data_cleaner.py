import pandas as pd


def basic_csv(path):
    df = pd.read_csv(path)
    return df