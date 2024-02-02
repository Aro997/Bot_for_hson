from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8ba9100c9256b35f0a089.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/48f4a67a59b41ea9e2c83.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AYYAY8")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AYYAY8")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1492530008").split()))


FAILED = "https://telegra.ph/file/8ba9100c9256b35f0a089.jpg"
