import requests
import json
from datetime import date
from envparse import env

TOKEN = env.str("TOKEN", default="")
ADMIN_CHAT_ID = 362857450
FILE_PATH = "standup_log.json"

with open(FILE_PATH, "r") as f_o:
    data_from_json = json.load(f_o)
    for user_id in data_from_json:
        if data_from_json[user_id]["last_updated_dt"] != str(date.today()):
            chat_id = data_from_json[user_id]["chat_id"]
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=Привет! Как насчёт того, чтобы постендапиться?)")
