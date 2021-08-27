import pandas as pd


def read_csv(file, cols_name):
    if cols_name is not None:
        df = pd.read_csv(file, usecols=cols_name)
    else:
        df = pd.read_csv(file)
    data = df.values
    return data


def write_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('../files/gccs2008-answer')
