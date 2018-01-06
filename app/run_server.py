# -*- coding: utf-8 -*-
"""
REST API starter (MAIN) module.

This file should contains (app)server configuration.
"""

from app.server import flask_app, PORT

if __name__ == '__main__':
    flask_app.run(debug=True, port=PORT)
