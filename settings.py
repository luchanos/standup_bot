import json

SECRETS_PATH = "secrets.json"

with open(SECRETS_PATH, "r") as f_o:
    secrets = json.load(f_o)

TOKEN = secrets["token"]
ADMIN_CHAT_ID = secrets["admin_chat_id"]
DATA_FILE_PATH = secrets["data_file_path"]
TELEGRAM_SERVICE_BASE_URL = secrets["telegram_service_base_url"]
