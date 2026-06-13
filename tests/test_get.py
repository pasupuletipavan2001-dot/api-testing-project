import requests
from utils.logger import log_message
from utils.config import BASE_URL

log_message("GET Test Started")

res = requests.get(f"{BASE_URL}/posts/1")

log_message(f"Status Code: {res.status_code}")

if res.status_code == 200:
    print("GET Status PASS")
else:
    print("GET Status FAIL")

data = res.json()

if data["id"] == 1:
    print("ID PASS")
else:
    print("ID FAIL")
log_message(data["title"])
log_message("GET Test Completed")