import requests
import random
import time

URL = "http://127.0.0.1:5000/api/data"

while True:
    payload = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }
    requests.post(URL, json=payload)
    print("Dados enviados:", payload)
    time.sleep(5)