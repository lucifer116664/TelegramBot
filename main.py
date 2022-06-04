from aiogram.utils import executor
from glue import dp
from dataBase import sqliteDB

async def on_startup(_):
    print('Bot is online...')
    sqliteDB.sqlStart()

from handlers import client, admin, general

client.registerHandlersClient(dp)
admin.registerHandlersAdmin(dp)
general.registerHandlersGeneral(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)