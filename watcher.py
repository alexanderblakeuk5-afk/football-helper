import time
from commands import get_last_message
from matcher import find_matches
from vk_sender import send_message
from vk_storage import (
    load_state,
    save_state
)


def check_schedule(force_check=False):

    print("Проверяю расписание...")

    state = load_state()

    team = state["team"]

    interval = state.get("interval", 5)

    last_check = state.get("last_check", 0)

    now = int(time.time())

    print("interval =", interval)
    print("last_check =", last_check)
    print("now =", now)

    old_team = state.get("active_team", team)

    force_check = False

    if state.get("command") == "CHECK":

        print("Получена команда CHECK")

        force_check = True

    if team != old_team:

        print(
            f"Команда изменена: {old_team} -> {team}"
        )

        force_check = True

    if not force_check:

        seconds_passed = now - last_check

        required_seconds = interval * 60

        if seconds_passed < required_seconds:

            print(
                f"Слишком рано. Осталось "
                f"{required_seconds - seconds_passed} сек."
            )

            return

    current_matches = find_matches(team)

    old_matches = state["matches"]

    if current_matches == old_matches and not force_check:

        print("Изменений нет")

        save_state(
            team,
            current_matches,
            state.get("interval", 5),
            "",
            now
        )

        return

    print("⚠ Расписание изменилось")

    message = (
        f"⚠ Изменение расписания\n\n"
        f"Команда: {team}\n\n"
    )

    for match in current_matches:

        message += (
            f"{match['date']}\n"
            f"{match['match']}\n\n"
        )

    send_message(message)

    save_state(
        team,
        current_matches,
        state.get("interval", 5),
        "",
        now
    )


if __name__ == "__main__":
    check_schedule()