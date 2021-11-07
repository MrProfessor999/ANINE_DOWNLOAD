import os
from telethon import TelegramClient

api_id = "7813081"
api_hash = "deccd07c38a5ec9fa0fa6e58790fe292"
bot_token = "2068737720:AAE7Om08wMG4Pj-PmRn7-9vukSk3sP7vsbA"

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
