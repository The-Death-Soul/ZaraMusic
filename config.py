# Zain Zara
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Evelina_Musicbot")
API_ID = int(getenv("API_ID", "8945070"))
API_HASH = getenv("API_HASH", "")
OWNER_NAME = getenv("OWNER_NAME", "zara_THE_addiction")
ALIVE_NAME = getenv("ALIVE_NAME", "DJ_Magical_World")
BOT_USERNAME = getenv("BOT_USERNAME", "Evelina_Musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DJ_Magical_World")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/+R7D0nHLk8s9jODA1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZaraSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5166884358 5102663914").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/bb7f23ae8d5024eb1c8b4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/The-Death-Soul/ZainMusic")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/d3185c725b9ba69b3f339.jpg")


