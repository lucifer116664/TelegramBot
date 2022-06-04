from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttonLoad = KeyboardButton('/Добавити')
buttonDelete = KeyboardButton('/Видалити')
buttonCancel = KeyboardButton('/Відміна')

KBAdmin1 = ReplyKeyboardMarkup(resize_keyboard=True)
KBAdmin1.row(buttonLoad, buttonDelete)

KBAdmin2 = ReplyKeyboardMarkup(resize_keyboard=True)
KBAdmin2.row(buttonCancel, buttonDelete)

deleteKB = InlineKeyboardMarkup(row_width=1)

mondayButton = InlineKeyboardButton(text='Понеділок', callback_data='deleteMonday')
tuesdayButton = InlineKeyboardButton(text='Вівторок', callback_data='deleteTuesday')
wednesdayButton = InlineKeyboardButton(text='Середа', callback_data='deleteWednesday')
thursdayButton = InlineKeyboardButton(text='Четвер', callback_data='deleteThursday')
fridayButton = InlineKeyboardButton(text='П`ятниця', callback_data='deleteFriday')

deleteKB.add(mondayButton, tuesdayButton, wednesdayButton, thursdayButton, fridayButton)
