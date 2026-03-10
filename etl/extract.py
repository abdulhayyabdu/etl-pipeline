import pandas as pd
import json


def read_csv(file_path):
    return pd.read_csv(file_path)


def read_json(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(json.loads(line))
    return data
