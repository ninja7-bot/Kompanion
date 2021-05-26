from telethon.sessions import StringSession
from telethon import TelegramClient

import os
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

#rom configparser import ConfigParser

#arser = ConfigParser()
#arser.read("config.ini")
#eneral = parser["general"]

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
SESSION = os.environ.get("SESSION")
    
#SESSION = general.get("SESSION")
#PP_ID = general.get("APP_ID")
#PI_HASH = general.get("API_HASH")
    
Kompanion = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
