from flask import Flask
from routes.users import users

app = Flask(__name__)
app.register_blueprint(users, url_prefix = '/api/users')
