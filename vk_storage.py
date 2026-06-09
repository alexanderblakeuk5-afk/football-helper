import json
import requests

from env_loader import (
    VK_USER_TOKEN,
    VK_GROUP_ID,
    VK_STATE_POST_ID
)

GROUP_ID = 239418802
POST_ID = 1


def load_state():

    response = requests.get(
        "https://api.vk.com/method/wall.getById",
        params={
            "posts": f"-{GROUP_ID}_{POST_ID}",
            "access_token": VK_USER_TOKEN,
            "v": "5.199"
        }
    )

    data = response.json()


    text = data["response"]["items"][0]["text"]

    json_text = text.replace(
        "[STATE]",
        ""
    ).strip()

    return json.loads(json_text)

from env_loader import (
    VK_USER_TOKEN,
    VK_GROUP_ID,
    VK_STATE_POST_ID
)

def save_state(matches):

    text = (
        "[STATE]\n\n" +
        json.dumps(
            {
                "matches": matches
            },
            ensure_ascii=False,
            indent=2
        )
    )

    response = requests.post(
        "https://api.vk.com/method/wall.edit",
        data={
            "owner_id": -int(VK_GROUP_ID),
            "post_id": int(VK_STATE_POST_ID),
            "message": text,
            "access_token": VK_USER_TOKEN,
            "v": "5.199"
        }
    )

    print(response.json())