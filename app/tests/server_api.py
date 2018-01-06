import requests
from app.client.api import ApiClient


def send_random_json_data_to_backend(client: ApiClient):
    response = requests.get("http://api.open-notify.org/astros.json")
    randomServerData = response.json()
    client.post_json_data('json', randomServerData)

    print(randomServerData)
