from matcher import find_matches
from vk_sender import send_message
from vk_storage import (
    load_state,
    save_state
)

TEAM = "Пермский период"


def check_schedule():

    print("Проверяю расписание...")

    current_matches = find_matches(TEAM)

    state = load_state()

    old_matches = state["matches"]

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

    save_state(current_matches)


if __name__ == "__main__":
    check_schedule()