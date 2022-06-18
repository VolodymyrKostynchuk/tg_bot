from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Загрузити')
b2 = KeyboardButton('/Видалити')
b3 = KeyboardButton('/Відміна')
b4 = KeyboardButton('/Повернутись')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(b1, b2, b3, b4)