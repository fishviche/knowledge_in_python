from crypt import methods
from flask import Blueprint

users = Blueprint("users", __name__)

@users.route('', methods = ['GET', 'POST'])
def home():
    return 'Hello world'