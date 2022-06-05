from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttonLoad = KeyboardButton('/Добавити')
buttonDelete = KeyboardButton('/Видалити')
buttonCancel = KeyboardButton('/Відміна')

KBAdmin1 = ReplyKeyboardMarkup(resize_keyboard=True)
KBAdmin1.row(buttonLoad, buttonDelete)

KBAdmin2 = ReplyKeyboardMarkup(resize_keyboard=True)
KBAdmin2.row(buttonCancel)

deleteKB = InlineKeyboardMarkup(row_width=1)
addKB = InlineKeyboardMarkup(row_width=1)

mondayDeleteButton = InlineKeyboardButton(text='Понеділок', callback_data='deleteMonday')
tuesdayDeleteButton = InlineKeyboardButton(text='Вівторок', callback_data='deleteTuesday')
wednesdayDeleteButton = InlineKeyboardButton(text='Середа', callback_data='deleteWednesday')
thursdayDeleteButton = InlineKeyboardButton(text='Четвер', callback_data='deleteThursday')
fridayDeleteButton = InlineKeyboardButton(text='П`ятниця', callback_data='deleteFriday')

mondayAddButton = InlineKeyboardButton(text='Понеділок', callback_data='addMonday')
tuesdayAddButton = InlineKeyboardButton(text='Вівторок', callback_data='addMonday')
wednesdayAddButton = InlineKeyboardButton(text='Середа', callback_data='addMonday')
thursdayAddButton = InlineKeyboardButton(text='Четвер', callback_data='addMonday')
fridayAddButton = InlineKeyboardButton(text='П`ятниця', callback_data='addMonday')

deleteKB.add(mondayDeleteButton, tuesdayDeleteButton, wednesdayDeleteButton, thursdayDeleteButton, fridayDeleteButton)
addKB.add(mondayAddButton, tuesdayAddButton, wednesdayAddButton, thursdayAddButton, fridayAddButton)
