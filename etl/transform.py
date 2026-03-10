import pandas as pd


def clean_csv(df):

    # convert timestamps
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['last_login'] = pd.to_datetime(
        df['last_login'], unit='s', errors='coerce')

    # boolean fix
    df['is_claimed'] = df['is_claimed'].replace({
        "True": True,
        "False": False,
        "truee": True
    })

    # numeric
    df['paid_amount'] = pd.to_numeric(
        df['paid_amount'], errors='coerce').round(2)

    # mask address (PII)
    df['address'] = df['address'].str.replace(r'[0-9]', 'X', regex=True)

    return df


def transform_json(data):

    users = []
    phones = []
    jobs = []

    for record in data:

        user = record.get("user_details", {})

        users.append({
            "user_id": record["user_id"],
            "name": user.get("name"),
            "dob": user.get("dob"),
            "username": user.get("username"),
            "created_at": record.get("created_at"),
            "updated_at": record.get("updated_at"),
            "logged_at": record.get("logged_at")
        })

        for phone in user.get("telephone_numbers", []):
            phones.append({
                "user_id": record["user_id"],
                "phone": phone
            })

        for job in record.get("jobs_history", []):
            jobs.append({
                "job_id": job.get("id"),
                "user_id": record["user_id"],
                "occupation": job.get("occupation"),
                "start": job.get("start"),
                "end": job.get("end")
            })

    return (
        pd.DataFrame(users),
        pd.DataFrame(phones),
        pd.DataFrame(jobs)
    )
