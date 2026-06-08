from env_loader import VK_USER_TOKEN
from datetime import datetime
from rapidfuzz import fuzz
import requests
from bs4 import BeautifulSoup
import re

def is_match(team_name, line):

    score = fuzz.partial_ratio(
        team_name.upper(),
        line.upper()
    )

    return score >= 90

MONTHS = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}

def parse_date(date_text):

    parts = date_text.split(",")

    date_part = parts[0].strip()

    day, month_name = date_part.split()

    return datetime(
        year=datetime.now().year,
        month=MONTHS[month_name.lower()],
        day=int(day)
    )

from datetime import datetime


def days_until(date_text):

    match_date = parse_date(date_text)

    today = datetime.now()

    delta = (match_date.date() - today.date()).days

    return delta

URL = "https://vk.com/nfl.perm?w=page-118923392_53372207"
USER_TOKEN = VK_USER_TOKEN

def get_schedule_html():

    response = requests.get(
        "https://api.vk.com/method/pages.get",
        params={
            "owner_id": -118923392,
            "page_id": 53372207,
            "need_html": 1,
            "access_token": USER_TOKEN,
            "v": "5.199"
        }
    )

    data = response.json()

    return data["response"]["html"]

def find_matches(team_name):

    html = get_schedule_html()

    fragment = html

    text = BeautifulSoup(
        fragment,
        "html.parser"
    ).get_text("\n")

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    current_date = None
    matches = []

    date_pattern = re.compile(
        r"^\d+\s+\w+"
    )

    team_upper = team_name.upper()

    for line in lines:

        if date_pattern.match(line):
            current_date = line
            continue

        if is_match(team_name, line):

            matches.append(
                {
                    "date": current_date,
                    "match": line
                }
            )

    return matches
