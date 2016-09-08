import requests
import json

url = "http://192.168.0.249/api/status"
method = "GET"
response = requests.request(method, url)
payload = json.loads(response.content)
print payload['code']