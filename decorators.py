import json

from settings import DATA_FILE_PATH


def user_checker(decorated_bot):
    def user_checker_inner(func):
        def inner(message):
            with open(DATA_FILE_PATH, "r") as f_o:
                data_from_json = json.load(f_o)
            user_id = str(message.from_user.id)
            if user_id not in data_from_json:
                decorated_bot.reply_to(message, text="Я вас ещё не знаю. Введите команду /start")
                return
            return func(message)
        return inner
    return user_checker_inner
