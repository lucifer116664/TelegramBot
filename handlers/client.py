from aiogram import types, Dispatcher
from glue import bot
from dataBase import sqliteDB
from buttonsAndKeyboards.clientKB import KBClient
import datetime

#Todays day definition:
dt = datetime.datetime.today()
day = ''
if dt.weekday() == 1:
    day = 'ВІВТОРОК'
elif dt.weekday() == 2:
    day = 'СЕРЕДУ'
elif dt.weekday() == 3:
    day = 'ЧЕТВЕР'
elif dt.weekday() == 4:
    day = 'ПЯТНИЦЮ'
else:
    day = 'ПОНЕДІЛОК'

async  def start(message: types.Message):
    startMsg = f'Здоровенькі були, {message.from_user.first_name}. Я - бот, що надасть Вам зручний доступ до розкладу уроків. Для того, щоб отримати розклад на той день, який Вас цікавить - '\
               f'просто натисніть на відповідну кнопку. Якщо ж Ви викладач і Вам потрібно внести корективи до розкладу - введіть команду /adminAccess (або ж натисніть на цей надпис). Якщо хочете '\
               f'повернутися до режиму перегляду - введіть команду /start або /help. Приємного користування!'
    try:
        await bot.send_message(message.from_user.id, startMsg, reply_markup=KBClient)
        await message.delete()
    except:
        message.reply('Щоб користуватися ботом, потрібно спочатку написати йому в пп: \nhttp://t.me/ProstoSuperskiyBot')

async def showToday(message: types.Message):
    await bot.send_message(message.from_user.id, f'РОЗКЛАД УРОКІВ НА {day}:')
    await sqliteDB.sqlRead(message)
    await message.delete()

async def showMonday(message: types.Message):
    await bot.send_message(message.from_user.id, 'РОЗКЛАД УРОКІВ НА ПОНЕДІЛОК:')
    await sqliteDB.sqlReadMonday(message)
    await message.delete()

async def showTuesday(message: types.Message):
    await bot.send_message(message.from_user.id, 'РОЗКЛАД УРОКІВ НА ВІВТОРОК:')
    await sqliteDB.sqlReadTuesday(message)
    await message.delete()

async def showWednesday(message: types.Message):
    await bot.send_message(message.from_user.id, 'РОЗКЛАД УРОКІВ НА СЕРЕДУ:')
    await sqliteDB.sqlReadWednesday(message)
    await message.delete()

async def showThursday(message: types.Message):
    await bot.send_message(message.from_user.id, 'РОЗКЛАД УРОКІВ НА ЧЕТВЕР:')
    await sqliteDB.sqlReadThursday(message)
    await message.delete()

async def showFriday(message: types.Message):
    await bot.send_message(message.from_user.id, 'РОЗКЛАД УРОКІВ НА П`ЯТНИЦЮ:')
    await sqliteDB.sqlReadFriday(message)
    await message.delete()

def registerHandlersClient(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(showToday, commands=['Сьогодні'])
    dp.register_message_handler(showMonday, commands=['Понеділок'])
    dp.register_message_handler(showTuesday, commands=['Вівторок'])
    dp.register_message_handler(showWednesday, commands=['Середа'])
    dp.register_message_handler(showThursday, commands=['Четвер'])
    dp.register_message_handler(showFriday, commands=['П`ятниця'])
