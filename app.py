import logging
import sys

from standup_bot import bot

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


while True:
    try:
        logger.info("Starting bot...")
        bot.polling()
    except Exception as err:
        msg = f"Restarting bot due to an error: {err}"
        bot.telegram_support_client.send_message_to_admin_chat(msg)
        logger.error(msg)
