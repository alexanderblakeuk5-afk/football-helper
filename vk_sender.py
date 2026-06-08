import requests
import random

from config_loader import config

TOKEN = config["vk_group_token"]
USER_ID = config["vk_user_id"]


def send_message(text):

    response = requests.post(
        "https://api.vk.com/method/messages.send",
        data={
            "user_id": USER_ID,
            "message": text,
            "random_id": random.randint(1, 1000000000),
            "access_token": TOKEN,
            "v": "5.199"
        }
    )

    return response.json()