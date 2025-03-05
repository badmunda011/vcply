import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
BOT_TOKEN = "7884528457:AAExu8m2N6oxiPvuug1uHcgWhntSncZhHK4"
STRING_SESSION = "BQGIzloAwMVAZC8FSxSWVwhUnzmyusp9MwEMMAnE8Bq3_KaQeuzA9OEg-COCBisfJZlBWw3ECDodQe8JzD5cilA2ppLDlC5VUjONUbyPB6Y3U0s_kMzvL3fHNSbclNGS7VKMLwBBkBqIdfREDFSXpJ4qvtxtdXXQKRkqqzS3sEOiocazJTp3qMpttAmlui5_2eJ1QIUuZtRVKOp8WZxbhDXQ2NWUrw1retvI0pm1e5FuAyMhrji6NhVlk2uVI9Fn4ByhGF0aHtzeBznaTe1GGf9pcgApLGC3UlAg6hVAZmUZhECEYLV7kYcqDvywx_hy-O5PVuHoBFdY8ETBwJ5iWH09vE8J3gAAAAGhzggHAA"
MONGO_DB_URL = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
LOG_GROUP_ID = -1002093247039


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())


# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 Hey, I am an advanced & superfast high quality userbot assistant with an upgraded version security system.\n\n🌿 I can't let you message my owner's dm without my owner's permission.\n\n🌺 My owner is offline now, please wait until my owner allows you.\n\n🍂 Please don't spam here, because spamming will force me to block you from my owner id.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/1217cb1e402b99fa47fdf.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Genius")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

