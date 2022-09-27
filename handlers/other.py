from aiogram import types, Dispatcher
from create_bot import dp

# listening for messages


# @dp.message_handler()
# async function to answer an incoming message
async def echo_send(message: types.Message):
    if message.text == "hello bot":
        await message.answer("hello human")
    else:
        await message.answer("hello world")
    # await message.answer(message.text) # just answer same text
    # await message.reply(message.text) # just answer same text and cite original message
    # await bot.send_message(message.from_user.id, message.text) # answer same text but to user as a dm


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
