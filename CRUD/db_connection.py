import os
import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        database="crudflask",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"]
    )

    # Create a cursor to perform database operations
    cur = conn.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(f'{conn.get_dsn_parameters()}\n')
    # Executing a SQL query
    cur.execute("SELECT version();")
    # Fetch result
    record = cur.fetchone()
    print(f"You are connected to - {record}\n")

except (Exception, Error) as error:
    print(f"Error while connecting to PostgreSQL {error}")
finally:
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")