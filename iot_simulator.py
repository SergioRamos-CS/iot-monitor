import requests
import random
import time

URL = "http://127.0.0.1:5000/api/data"

while True:
    payload = {
        # Temperatura entre 35°C e 40°C
        "temperature": round(random.uniform(37, 38), 2),

        # Umidade relativa entre 45% e 65%
        "humidity": round(random.uniform(50, 60), 2)
    }

    requests.post(URL, json=payload)
    print("Dados enviados:", payload)
    time.sleep(5)