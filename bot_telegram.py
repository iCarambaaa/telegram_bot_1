from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot is online")


'''***************************************CLIENT PART***************************************'''


@dp.message_handler(commands=["start", "help"])
async def command_start(message: types.Message):
    # as telegram bots aren't allowed to start conversation and the send_message handler is used we need to a try and catch here
    try:
        await bot.send_message(message.from_user.id, "good appetite")
        await message.delete()  # delete user command in chat
    except:
        message.reply(
            "No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot")


@dp.message_handler(commands=["time"])
async def command_time(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "10:00 - 23:00")
        # await message.delete()
    except:
        message.reply(
            "No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot")


@dp.message_handler(commands=["location"])
async def command_location(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Prinz Street 132, New London")
        # await message.delete()
    except:
        message.reply(
            "No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot")


'''***************************************ADMIN PART****************************************'''


'''***************************************MAIN PART***************************************'''
# listening for messages


@dp.message_handler()
# async function to answer an incoming message
async def echo_send(message: types.Message):
    if message.text == "hello bot":
        await message.answer("hello human")
    # await message.answer(message.text) # just answer same text
    # await message.reply(message.text) # just answer same text and cite original message
    # await bot.send_message(message.from_user.id, message.text) # answer same text but to user as a dm

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
