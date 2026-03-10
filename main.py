from etl.extract import read_csv, read_json
from etl.transform import clean_csv, transform_json
from etl.load import load_table


def run_pipeline():
    # CSV
    csv_data = read_csv("data/test.csv")
    csv_clean = clean_csv(csv_data)
    load_table(csv_clean, "test")

    # JSON
    json_data = read_json("data/test.json")

    users, phones, jobs = transform_json(json_data)

    load_table(users, "users")
    load_table(phones, "telephone_numbers")
    load_table(jobs, "jobs_history")


if __name__ == "__main__":
    run_pipeline()
