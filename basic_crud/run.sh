#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
export DB_USERNAME="crudflask_user"
export DB_PASSWORD="cR7d.@us3r"
gunicorn --bind 0.0.0.0:5000 index:app