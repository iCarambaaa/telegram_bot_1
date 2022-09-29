from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import sqlite_db

# @dp.message_handler(commands=["start", "help"])


async def command_start(message: types.Message):
    # as telegram bots aren't allowed to start conversation and the send_message handler is used we need to a try and catch here
    try:
        await bot.send_message(message.from_user.id, "good appetite", reply_markup=kb_client)
        await message.delete()  # delete user command in chat
    except:
        message.reply(
            "No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot")


# @dp.message_handler(commands=["time"])
async def command_time(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "10:00 - 23:00")
        # await message.delete()
    except:
        message.reply(
            'No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot')


# @dp.message_handler(commands=["location"])
async def command_location(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Prinz Street 132, New London", reply_markup=ReplyKeyboardRemove())
        # await message.delete()
    except:
        message.reply(
            'No dm before user started private conversation first:\nhttps://t.me/@testing_pizza089_bot')


# @dp.message_handler(commands=["menu"])
async def command_menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start", "help"])
    dp.register_message_handler(command_time, commands=["time"])
    dp.register_message_handler(command_location, commands=["location"])
    dp.register_message_handler(command_menu, commands=["menu"])
