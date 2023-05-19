import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID","21166181"))
    API_HASH = os.environ.get("API_HASH", "8c3a80939d1a3ca93acfee34ae66e267")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6119015832:AAG3KpguH0E1Fe6L7vnpFwDUBE94-_b9Q2E")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Snapstoriesdown_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
