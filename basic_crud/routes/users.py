from psycopg2.extras import RealDictCursor
from flask import Blueprint, request
from utils.connection_db import get_db_connection

users = Blueprint("users", __name__)


@users.route("", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        get_users = """
        SELECT
            fullname, email, phone
        FROM
            users
        """
        cur.execute(get_users)
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
