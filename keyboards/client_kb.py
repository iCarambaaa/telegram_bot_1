from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# ReplyKeyboardRemove removes the keyboard

b1 = KeyboardButton("/Time")
b2 = KeyboardButton("/Location")
b3 = KeyboardButton("/Menu")
# b4 = KeyboardButton("Telephone", request_contact=True) # request user number
# b5 = KeyboardButton("My Location", request_location=True) # request user location
# one_time_keyboard=True hides buttons after clicking
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

# add for new line
# insert for same line
# row for all in one row
# mix and combine as you like
kb_client.add(b1).add(b2).insert(b3)
#kb_client.row(b4, b5)
