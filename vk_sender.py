import requests
import random

from env_loader import (
    VK_GROUP_TOKEN,
    VK_USER_ID
)

def send_message(text):

    response = requests.post(
        "https://api.vk.com/method/messages.send",
        data={
            "user_id": VK_USER_ID,
            "message": text,
            "random_id": random.randint(
                1,
                1000000000
            ),
            "access_token": VK_GROUP_TOKEN,
            "v": "5.199"
        }
    )

    print(response.json())


print("TOKEN =", VK_GROUP_TOKEN)
print("USER_ID =", VK_USER_ID)

if __name__ == "__main__":
    send_message("Тест из vk_sender.py")