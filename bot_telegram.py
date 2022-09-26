from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# listening for messages


@dp.message_handler()
# async function to answer an incoming message
async def echo_send(message: types.Message):
    if message.text == "hello bot":
        await message.answer("hello human")
    # await message.answer(message.text) # just answer same text
    # await message.reply(message.text) # just answer same text and cite original message
    # await bot.send_message(message.from_user.id, message.text) # answer same text but to user as a dm

executor.start_polling(dp, skip_updates=True)
