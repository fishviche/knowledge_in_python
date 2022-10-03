#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
export DB_USERNAME="crudflask_user"
export DB_PASSWORD="cR7d.@us3r"
export DB_HOST="localhost"
export DB_PORT="5435"
# python3 -m pytest
gunicorn --bind 0.0.0.0:5011 --log-level=DEBUG --reload index:app