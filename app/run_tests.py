# -*- coding: utf-8 -*-
"""
Tests module.

Tests execution.
"""

from app.client import client
from app.tests.server_api import send_random_json_data_to_backend


if __name__ == '__main__':
    send_random_json_data_to_backend(client)
