import requests
import json
from utils.logger import log_message
from utils.config import BASE_URL

log_message("POST Test Started")

with open("data/payload.json", "r") as file:
    payload = json.load(file)

res = requests.post(
    f"{BASE_URL}/posts",
    json=payload
)

log_message(f"Status Code: {res.status_code}")

if res.status_code == 201:
    print("POST Status PASS")
else:
    print("POST Status FAIL")

response_data = res.json()

if response_data["title"] == payload["title"]:
    print("POST Data PASS")
else:
    print("POST Data FAIL")

log_message("POST Test Completed")