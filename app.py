import json
import streamlit as st

from matcher import find_matches

from matcher import days_until

with open(
    "settings.json",
    "r",
    encoding="utf-8"
) as f:
    settings = json.load(f)

st.set_page_config(
    page_title="Футбольный помощник"
)

st.title("⚽ Футбольный помощник")

team = st.text_input(
    "Введите название команды",
    value=settings["favorite_team"]
)

if st.button("⭐ Сделать моей командой"):

    settings["favorite_team"] = team

    with open(
        "settings.json",
        "w",
        encoding="utf-8"
    ) as f:

        import json

        json.dump(
            settings,
            f,
            ensure_ascii=False,
            indent=4
        )

    st.success("Команда сохранена")

if st.button("Найти матчи"):

    with st.spinner(
        "Загружаю расписание..."
    ):

        matches = find_matches(team)

    if not matches:

        st.warning(
            "Матчи не найдены"
        )

    else:

        st.success(
            f"Найдено матчей: {len(matches)}"
        )

        for item in matches:

            days = days_until(item["date"])

            if days == 0:
                badge = "🔥 Сегодня"
            elif days == 1:
                badge = "⏳ Завтра"
            else:
                badge = f"📅 Через {days} дн."

            st.markdown(
                f"""
### {badge}

**{item['date']}**

{item['match']}
"""
    )