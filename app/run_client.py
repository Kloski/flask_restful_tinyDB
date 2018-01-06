import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

print(data)
