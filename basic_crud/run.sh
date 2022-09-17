#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
export DB_USERNAME="crudflask_user"
export DB_PASSWORD="cR7d.@us3r"
flask run --port=5001 --host=0.0.0.0