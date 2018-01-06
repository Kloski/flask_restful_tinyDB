#!/bin/bash

# defines the main script to be executed by Flask
export FLASK_APP=./app/run_server.py
export FLASK_DEBUG=true

# activates the virtual environment
source $(pipenv --venv)/bin/activate

# http://flask.pocoo.org/docs/0.12/cli/
# run our Flask application listening to all interfaces on the computer (-h 0.0.0.0)
# flask run -h 127.0.0.1
flask run
