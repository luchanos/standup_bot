import requests

TOKEN = "5200212331:AAHYPoA56yoKQ9Gf0lQuaxUoo3FtXdIY7qg"
ADMIN_CHAT_ID = 362857450
requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text=завожу бота")
