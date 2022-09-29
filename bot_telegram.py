from aiogram.utils import executor
from create_bot import dp
from database import sqlite_db
from handlers import client, admin, other


async def on_startup(_):
    print("Bot is online")
    sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
# as this one is empty (no commands) import always last
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
