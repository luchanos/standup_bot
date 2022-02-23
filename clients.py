import requests
import logging

from utils import append_slash
from telebot import TeleBot

logger = logging.getLogger(__name__)


class TelegramSupportClient:
    """
    Клиент для сервисных взаимодействий с Телеграм
    """

    def __init__(self, base_url: str, token: str, admin_chat_id: int, *args, **kwargs):
        self.base_url = append_slash(base_url)
        self.token = token
        self.admin_chat_id = admin_chat_id

    def create_admin_send_msg_url(self, message: str) -> str:
        return f"{self.base_url}bot{self.token}/sendMessage?chat_id={self.admin_chat_id}&text={message}"

    def create_send_msg_url(self, message: str, chat_id: int) -> str:
        return f"{self.base_url}bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"

    def send_message_to_chat(self, chat_id: int, message: str):
        url = self.create_send_msg_url(message=message, chat_id=chat_id)
        return requests.get(url)

    def send_message_to_admin_chat(self, message):
        # todo luchanos возможно тут стоит рэйзить исключение
        if self.admin_chat_id is None:
            logger.error("No admin chat id had been set to telegram client!")
            return
        url = self.create_admin_send_msg_url(message)
        # todo luchanos а вот тут десериализацию и проверку положительного ответа схемой
        return requests.get(url)


class StandupTelegramBot(TeleBot):
    """Класс для расширенной работы с ботом Телеграм"""

    def __init__(self, token: str, telegram_support_client: TelegramSupportClient):
        super().__init__(token)
        self.telegram_support_client = telegram_support_client
