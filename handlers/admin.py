from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import AdminID
from glue import bot, dp
from  buttonsAndKeyboards.clientKB import urlKB1
from buttonsAndKeyboards.adminKB import KBAdmin1, KBAdmin2, deleteKB
from dataBase.sqliteDB import sqlAdd
from dataBase import sqliteDB

class FSMAdmin(StatesGroup):
    ID = State()
    Subject = State()
    Teacher = State()
    StartTime = State()
    EndTime = State()
    Link = State()
    Class = State()

async def adminAccess(message: types.Message):
    if message.from_user.id != AdminID:
        await message.answer('У Вас немає доступу.')
        await message.delete()
        await State.finish()
    else:
        await bot.send_message(message.from_user.id, 'Що Ви бажаєте зробити?', reply_markup=KBAdmin1)
        await message.delete()

#New table line enterance:
async def enterNewLine(message: types.Message):
    if message.from_user.id != AdminID:
        await message.ansewr('У Вас немає доступу для внесення даних.')
        await message.delete()
        await State.finish()
    else:
        await FSMAdmin.ID.set()
        await message.answer('Введіть ID:', reply_markup=KBAdmin2)
        await message.delete()

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Ввід даних відмінено.', reply_markup=KBAdmin1)
    await message.delete()

async def enterID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ID'] = int(message.text)
    await FSMAdmin.next()
    await message.answer('Введіть назву уроку:')

async def enterSubject(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Subject'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть ім`я викладача:')

async def enterTeacher(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Teacher'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть час початку уроку:')

async def enterStartTime(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['StartTime'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть час закінчення уроку:')

async def enterEndTime(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['EndTime'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть посилання на урок:')

async def enterLink(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Link'] = message.text
    await FSMAdmin.next()
    await message.answer('Введіть номер та букву класу (наприклад 7Б):')

async def enterClass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Class'] = message.text
    await sqlAdd(state)
    await state.finish()

async def delete(message: types.Message):
    if message.from_user.id != AdminID:
        await message.ansewr('У Вас немає доступу для видалення даних.')
        await message.delete()
        await State.finish()
    else:
        await bot.send_message(message.from_user.id, 'Запис у якому дні тиждня Ви хочете видалити?', reply_markup=deleteKB)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def delMonadyRun(callbackQuery: types.CallbackQuery):
    await sqliteDB.sqlDeleteMonday(callbackQuery.data.replace('del ', ''))
    await callbackQuery.answer(text=f'{callbackQuery.data.replace("del ", "")} урок видалено з розкладу.', show_alert=True)

@dp.callback_query_handler(text='deleteMonday')
async def deleteMonday(message: types.Message, callback: types.CallbackQuery):
    read = await sqliteDB.sqlSelectMonday()
    for ret in read:
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
        await bot.send_message(message.from_user.id, text='__________^^^__________', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[0]} урок', callback_data=f'del {ret[0]}')))
    callback.answer()

@dp.callback_query_handler(text='deleteTuesday')
async def deleteTuesday(message: types.Message, callback: types.CallbackQuery):
    read = await sqliteDB.sqlSelectTuesday()
    for ret in read:
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
        await bot.send_message(message.from_user.id, text='__________^^^__________', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[0]} урок', callback_data=f'del {ret[0]}')))
    callback.answer()

@dp.callback_query_handler(text='deleteWednesday')
async def deleteWednesday(message: types.Message, callback: types.CallbackQuery):
    read = await sqliteDB.sqlSelectWednesday()
    for ret in read:
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
        await bot.send_message(message.from_user.id, text='__________^^^__________', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[0]} урок', callback_data=f'del {ret[0]}')))
    callback.answer()

@dp.callback_query_handler(text='deleteThursday')
async def deleteThursday(message: types.Message, callback: types.CallbackQuery):
    read = await sqliteDB.sqlSelectThursday()
    for ret in read:
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
        await bot.send_message(message.from_user.id, text='__________^^^__________', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[0]} урок', callback_data=f'del {ret[0]}')))
    callback.answer()

@dp.callback_query_handler(text='deleteFriday')
async def deleteFriday(message: types.Message, callback: types.CallbackQuery):
    read = await sqliteDB.sqlSelectFriday()
    for ret in read:
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
        await bot.send_message(message.from_user.id, text='__________^^^__________', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[0]} урок', callback_data=f'del {ret[0]}')))
    callback.answer()


def registerHandlersAdmin(dp: Dispatcher):
    dp.register_message_handler(adminAccess, commands='adminAccess', state=None)
    dp.register_message_handler(enterNewLine, commands='Добавити', state=None)
    dp.register_message_handler(cancel, state="*", commands='Відміна')
    dp.register_message_handler(cancel, Text(equals='Відміна', ignore_case=True), state="*")
    dp.register_message_handler(delete, commands='Видалити', state=None)
    dp.register_message_handler(enterID, state=FSMAdmin.ID)
    dp.register_message_handler(enterSubject, state=FSMAdmin.Subject)
    dp.register_message_handler(enterTeacher, state=FSMAdmin.Teacher)
    dp.register_message_handler(enterStartTime, state=FSMAdmin.StartTime)
    dp.register_message_handler(enterEndTime, state=FSMAdmin.EndTime)
    dp.register_message_handler(enterLink, state=FSMAdmin.Link)
    dp.register_message_handler(enterClass, state=FSMAdmin.Class)
