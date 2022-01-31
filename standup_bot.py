from telebot import TeleBot
import json
from datetime import date
from envparse import Env

env = Env()

TOKEN = env.str("TOKEN")

bot = TeleBot(TOKEN)


def standup_speech(message):
    with open("standup_log.json", "r") as f_o:
        data_from_json = json.load(f_o)

    data_from_json[str(date.today())] = message.text

    with open("standup_log.json", "w") as f_o:
        json.dump(data_from_json, f_o)

    bot.reply_to(message, text="Отлично! Хорошего дня!")


@bot.message_handler(commands=["standup_speech"])
def standuper(message):
    bot.reply_to(message, text="Чем занимался вчера? Чем будешь заниматься сегодня? Есть ли какие-нибудь трудности?")
    bot.register_next_step_handler(message, standup_speech)


while True:
    try:
        print("Завожу бота")
        bot.polling()
    except Exception as err:
        print("Перезавожу бота", err)
