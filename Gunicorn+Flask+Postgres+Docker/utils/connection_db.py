import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database="crudflask",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"]
    )
    return conn
