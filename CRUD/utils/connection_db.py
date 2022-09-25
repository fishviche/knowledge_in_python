import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        database="crudflask",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"]
    )
    return conn
