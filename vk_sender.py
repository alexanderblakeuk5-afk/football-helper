import requests
import random

from env_loader import VK_GROUP_TOKEN, VK_USER_ID

params = {
    "access_token": VK_GROUP_TOKEN,
    "v": "5.199",
    "peer_id": VK_USER_ID,
    "message": message
}


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