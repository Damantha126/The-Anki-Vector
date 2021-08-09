import os
import asyncio
import traceback
from pyrogram import Client, filters
from AnkiVector import BOT_TOKEN, API_ID, API_HASH
from pyrogram.types import Message
from handlers.broadcast_handlers import main_broadcast_handler

Bot = Client(bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(BOT_OWNER) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)
