from telebot import TeleBot
import json
from datetime import date
from envparse import Env
import requests

env = Env()

TOKEN = env.str("TOKEN")

bot = TeleBot(TOKEN)
ADMIN_CHAT_ID = 362857450
FILE_PATH = "standup_log.json"


def standup_speech(message):
    with open(FILE_PATH, "r") as f_o:
        data_from_json = json.load(f_o)

    user_id = str(message.from_user.id)
    if user_id not in data_from_json:
        bot.reply_to(message, text="Я вас ещё не знаю. Введите команду /start")
        return

    data_from_json[user_id]["last_updated_dt"] = str(date.today())

    with open(FILE_PATH, "w") as f_o:
        json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)

    bot.reply_to(message, text="Отлично! Хорошего дня!")

    msg_to_admin = f"Пользователь @{data_from_json[user_id]['username']} говорит: {message.text}"
    bot.send_message(ADMIN_CHAT_ID, text=msg_to_admin)


@bot.message_handler(commands=["standup_speech"])
def standuper(message):
    bot.reply_to(message, text="Чем занимался вчера? Чем будешь заниматься сегодня? Есть ли какие-нибудь трудности?")
    bot.register_next_step_handler(message, standup_speech)


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.chat.username
    with open(FILE_PATH, "r") as f_o:
        data_from_json = json.load(f_o)
    if str(user_id) not in data_from_json:
        data_from_json[user_id] = {
            "last_updated_dt": None,
            "chat_id": chat_id,
            "username": username
        }
        with open(FILE_PATH, "w") as f_o:
            json.dump(data_from_json, f_o, indent=4, ensure_ascii=False)
        bot.reply_to(message, text="Добро пожаловать!")
    else:
        bot.reply_to(message, text="И снова здравствуйте!")


while True:
    try:
        print("Завожу бота")
        bot.polling()
    except Exception as err:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text=Произошла ошибка: {err})")
        print("Перезавожу бота", err)
