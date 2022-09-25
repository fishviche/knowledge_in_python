import psycopg2
from utils.connection_db import get_db_connection


def _apply_migrations(server, cur, conn):
    server.log.info("Attempting to create migration table")
    with open("./sql/1_table.sql", "r") as f:
        sentences = [x.replace("\n", "") + ";" for x in f.read().rsplit(";") if x != ""]
    for sentence in sentences:
        try:
            cur.execute(sentence)
            server.log.info("=> Table created")
            conn.commit()
        except psycopg2.errors.DuplicateTable:
            server.log.info("=> Table exists")
    cur.close()
    conn.close()


def when_ready(server):
    server.log.info("Server is ready")
    conn = get_db_connection()
    cur = conn.cursor()
    _apply_migrations(server, cur, conn)
    server.log.info("Spawning workers")
