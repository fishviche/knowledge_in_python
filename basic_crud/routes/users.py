from psycopg2.extras import RealDictCursor
from flask import Blueprint, request
from utils.connection_db import get_db_connection
from models.users import get_user, insert_user

users = Blueprint("users", __name__)


@users.route("", methods=["GET", "POST"])
def all_users():
    if request.method == "GET":
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        response = get_user(cur)
        return response
    if request.method == "POST":
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        response = insert_user(request.get_json(), cur)
        conn.commit()
        return response
    cur.close()
    conn.close()


@users.route("/user", methods=["GET", "PUT", "DELETE"])
def one_user():
    if request.method == "GET":
        user_id = request.values.get("id")
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        response = get_user(cur, int(user_id))
        return response
    if request.method == "PUT":
        return
    cur.close()
    conn.close()
