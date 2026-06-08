import json

from matcher import find_matches
from vk_sender import send_message

TEAM = "Пермский период"


def check_schedule():

    print("Проверяю расписание...")

    current_matches = find_matches(TEAM)

    with open(
        "data/last_matches.json",
        "r",
        encoding="utf-8"
    ) as f:

        old_matches = json.load(f)

    if current_matches == old_matches:

        print("Изменений нет")
        return

    print("⚠ Расписание изменилось")

    message = (
        f"⚠ Изменение расписания\n\n"
        f"Команда: {TEAM}\n\n"
    )

    for match in current_matches:

        message += (
            f"{match['date']}\n"
            f"{match['match']}\n\n"
        )

    send_message(message)

    with open(
        "data/last_matches.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            current_matches,
            f,
            ensure_ascii=False,
            indent=4
        )


if __name__ == "__main__":
    check_schedule()