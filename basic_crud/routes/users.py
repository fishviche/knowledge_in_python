from psycopg2.extras import RealDictCursor
from flask import Blueprint, request
from utils.connection_db import get_db_connection
from models.users import insert_user

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
        return users
    if request.method == "POST":
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        response = insert_user(request.get_json(), cur)
        conn.commit()
        return response
    cur.close()
    conn.close()