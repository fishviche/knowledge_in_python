from crypt import methods
from flask import Blueprint
from utils.connection_db import get_db_connection

users = Blueprint("users", __name__)

@users.route('', methods = ['GET', 'POST'])
def home():
    return 'Hello world'