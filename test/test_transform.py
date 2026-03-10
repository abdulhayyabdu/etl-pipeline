from etl.transform import clean_csv
import pandas as pd


def test_paid_amount():

    df = pd.DataFrame({
        "paid_amount": ["100.123"]
    })

    result = clean_csv(df)

    assert result["paid_amount"][0] == 100.12
