import datetime
from dataclasses import asdict

from clients import TelegramSupportClient, StandupTelegramBot
from decorators import user_checker
from models import UserData
from settings import TELEGRAM_SERVICE_BASE_URL, TOKEN, ADMIN_CHAT_ID, DATA_FILE_PATH
import json
from datetime import date

telegram_support_client = TelegramSupportClient(base_url=TELEGRAM_SERVICE_BASE_URL,
                                                token=TOKEN,
                                                admin_chat_id=ADMIN_CHAT_ID)
bot = StandupTelegramBot(TOKEN, telegram_support_client)


def get_actual_data() -> dict:
    with open(DATA_FILE_PATH, "r") as f_o:
        data_from_json = json.load(f_o)
    return data_from_json


def refresh_actual_data(actual_data: dict) -> None:
    with open(DATA_FILE_PATH, "w") as f_o:
        json.dump(actual_data, f_o, indent=4, ensure_ascii=False)


def standup_speech(message):
    actual_data = get_actual_data()
    user_id = str(message.from_user.id)
    actual_data[user_id]["last_updated_dt"] = str(date.today())
    refresh_actual_data(actual_data)
    bot.reply_to(message, text="Отлично! Хорошего дня!")
    msg_to_admin = f"Пользователь @{actual_data[user_id]['username']} говорит: {message.text}"
    bot.send_message(ADMIN_CHAT_ID, text=msg_to_admin)


@bot.message_handler(commands=["standup_speech"])
@user_checker(bot)
def standuper(message):
    bot.reply_to(message, text="Чем занимался вчера? Чем будешь заниматься сегодня? Есть ли какие-нибудь трудности?")
    bot.register_next_step_handler(message, standup_speech)


@bot.message_handler(commands=["time_it"])
@user_checker(bot)
def time_it(message):
    time_answer_mapper = {
        "start": "Вы начали заниматься",
        "stop": "Вы закончили заниматься"
    }
    user_id = str(message.from_user.id)
    actual_data = get_actual_data()
    dt = datetime.datetime.now()
    total_programming_time = actual_data[user_id]["total_programming_time"]
    event = "start" if not total_programming_time or total_programming_time[-1]["event"] == "stop" else "stop"
    d = {
        "dt": str(dt),
        "event": event
    }
    actual_data[user_id]["total_programming_time"].append(d)
    refresh_actual_data(actual_data)
    bot.reply_to(message, text=time_answer_mapper[event])


@bot.message_handler(commands=["start"])
def start(message):
    """
    Проверяем, зарегистрирован ли пользователь в нашей системе.
    Если да - приветствуем его. Если нет - регистрируем и привествуем.
    """
    user_id = message.from_user.id
    actual_data = get_actual_data()
    if str(user_id) not in actual_data:
        user_data = UserData(chat_id=message.chat.id,
                             username=message.chat.username)
        actual_data[user_id] = asdict(user_data)
        refresh_actual_data(actual_data)
        bot.reply_to(message, text="Добро пожаловать! Регистрация прошла успешно!")
    else:
        bot.reply_to(message, text="И снова здравствуйте! Вы уже зарегистрированы!")
