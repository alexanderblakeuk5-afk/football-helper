import requests

from env_loader import (
    VK_GROUP_TOKEN,
    VK_GROUP_ID
)


def get_last_message():

    response = requests.get(
        "https://api.vk.com/method/messages.getConversations",
        params={
            "access_token": VK_GROUP_TOKEN,
            "v": "5.199",
            "count": 1
        }
    )

    data = response.json()

    message = (
        data["response"]
        ["items"][0]
        ["last_message"]
    )

    return {
        "id": message["conversation_message_id"],
        "text": message["text"]
    }