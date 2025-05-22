import requests
from config import API_TOKEN

headers = {"Authorization": f"Bearer {API_TOKEN}"}

import requests
from config import API_TOKEN, API_URL, MODEL_NAME

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def send_message_to_model(prompt):
    payload = {
        "messages": [{"role": "user", "content": f'{prompt}'}],
        "model": MODEL_NAME
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]