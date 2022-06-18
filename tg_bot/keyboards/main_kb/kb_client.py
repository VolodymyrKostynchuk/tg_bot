from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Розклад_пар')
b2 = KeyboardButton('/Розклад_дзвінків')
b3 = KeyboardButton('/Список_студентів')
b4 = KeyboardButton('/Список_викладачів')
b5 = KeyboardButton('/Адреса')
b6 = KeyboardButton('/Новини')
b7 = KeyboardButton('/Керівники_диплому')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(b1, b2, b3).row(b4, b5, b6).add(b7)