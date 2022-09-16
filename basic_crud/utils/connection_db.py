import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(host="", database="",user='',password='')
