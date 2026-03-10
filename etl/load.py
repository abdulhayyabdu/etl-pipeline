from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/etl_db"
)


def load_table(df, table_name):
    with engine.begin() as conn:
        df.to_sql(
            name=table_name,
            con=conn,
            if_exists="replace",
            index=False
        )
