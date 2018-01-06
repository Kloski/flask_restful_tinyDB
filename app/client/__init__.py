from app.server import PORT

BACKEND_URL = f"http://127.0.0.1:{PORT}/api/"

from app.client.api import ApiClient

client = ApiClient(BACKEND_URL)
