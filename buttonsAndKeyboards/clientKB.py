from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttonShowToday = KeyboardButton('/Сьогодні')
buttonShowMonday = KeyboardButton('/Понеділок')
buttonShowTuesday = KeyboardButton('/Вівторок')
buttonShowWednesday = KeyboardButton('/Середа')
buttonShowThursday = KeyboardButton('/Четвер')
buttonShowFriday = KeyboardButton('/П`ятниця')

KBClient = ReplyKeyboardMarkup(resize_keyboard=True)
KBClient.row(buttonShowToday).row(buttonShowMonday, buttonShowTuesday, buttonShowWednesday).row(buttonShowThursday, buttonShowFriday)

urlKB1 = InlineKeyboardMarkup(row_width=1)
urlKB2 = InlineKeyboardMarkup(row_width=1)

urlButton1 = InlineKeyboardButton(text='Посилання на урок', url='https://youtu.be/dQw4w9WgXcQ')
urlButton2 = InlineKeyboardButton(text='Посилання на урок', url='https://youtu.be/eMCJKclUvWQ?t=53')

urlKB1.add(urlButton1)
urlKB2.add(urlButton2)

