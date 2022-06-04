from aiogram import types, Dispatcher
from glue import dp
import json

async def antiMat(message : types.Message):
    if{i.lower() for i in message.text.split(' ')} .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply("Ввічливі люди таких слів не використовують!!!")
        await message.delete()

def registerHandlersGeneral(dp : Dispatcher):
    dp.register_message_handler(antiMat)