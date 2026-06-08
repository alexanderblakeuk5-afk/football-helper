import os
import json

if os.path.exists("config.json"):

    with open(
        "config.json",
        "r",
        encoding="utf-8"
    ) as f:

        config = json.load(f)

    VK_USER_TOKEN = config["vk_user_token"]
    VK_GROUP_TOKEN = config["vk_group_token"]
    VK_USER_ID = config["vk_user_id"]

else:

    VK_USER_TOKEN = os.getenv("VK_USER_TOKEN")
    VK_GROUP_TOKEN = os.getenv("VK_GROUP_TOKEN")
    VK_USER_ID = os.getenv("VK_USER_ID")