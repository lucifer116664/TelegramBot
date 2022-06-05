import sqlite3 as sql
from glue import bot
from buttonsAndKeyboards.clientKB import urlKB1, urlKB2
import datetime

dt = datetime.datetime.today()

def sqlStart():
    global base, cursor
    base = sql.connect('school.db')
    cursor = base.cursor()
    if base:
        print('DB is connected correctly...')
    else:
        print('DB CONNECTION ERROR!!!')
    base.execute('CREATE TABLE IF NOT EXISTS Monday(ID INT PRIMARY KEY, Subject TEXT, Teacher TEXT, StartTime TEXT, EndTime TEXT, Link TEXT, Class TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS Tuesday(ID INT PRIMARY KEY, Subject TEXT, Teacher TEXT, StartTime TEXT, EndTime TEXT, Link TEXT, Class TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS Wednesday(ID INT PRIMARY KEY, Subject TEXT, Teacher TEXT, StartTime TEXT, EndTime TEXT, Link TEXT, Class TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS Thursday(ID INT PRIMARY KEY, Subject TEXT, Teacher TEXT, StartTime TEXT, EndTime TEXT, Link TEXT, Class TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS Friday(ID INT PRIMARY KEY, Subject TEXT, Teacher TEXT, StartTime TEXT, EndTime TEXT, Link TEXT, Class TEXT)')
    base.commit()

async def sqlAddMonday(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO Monday VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sqlAddTuesday(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO Tuesday VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sqlAddWednesday(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO Wednesday VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sqlAddThursday(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO Thursday VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sqlAddFriday(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO Friday VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sqlRead(message):
    if dt.weekday() == 1:
        for ret in cursor.execute('SELECT * FROM Tuesday').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
    elif dt.weekday() == 2:
        for ret in cursor.execute('SELECT * FROM Wednesday').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
    elif dt.weekday() == 3:
        for ret in cursor.execute('SELECT * FROM Thursday').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
    elif dt.weekday() == 4:
        for ret in cursor.execute('SELECT * FROM Friday').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)
    else:
        for ret in cursor.execute('SELECT * FROM Monday').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlSelectMonday():
    return cursor.execute('SELECT * FROM Monday').fetchall()

async def sqlSelectTuesday():
    return cursor.execute('SELECT * FROM Tuesday').fetchall()

async def sqlSelectWednesday():
    return cursor.execute('SELECT * FROM Wednesday').fetchall()

async def sqlSelectThursday():
    return cursor.execute('SELECT * FROM Thursday').fetchall()

async def sqlSelectFriday():
    return cursor.execute('SELECT * FROM Friday').fetchall()

async def sqlReadMonday(message):
    for ret in cursor.execute('SELECT * FROM Monday').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlReadTuesday(message):
    for ret in cursor.execute('SELECT * FROM Tuesday').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlReadWednesday(message):
    for ret in cursor.execute('SELECT * FROM Wednesday').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlReadThursday(message):
    for ret in cursor.execute('SELECT * FROM Thursday').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlReadFriday(message):
    for ret in cursor.execute('SELECT * FROM Friday').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]} - {ret[1]}\nВчитель: {ret[2]}\nПочаток: {ret[3]}\nКінець: {ret[4]}\n', reply_markup=urlKB1)

async def sqlDeleteMonday(data):
    cursor.execute('DELETE FROM Monday WHERE ID == ?', (data,))
    base.commit()

async def sqlDeleteTuesday(data):
    cursor.execute('DELETE FROM Tuesday WHERE ID == ?', (data,))
    base.commit()

async def sqlDeleteWednesday(data):
    cursor.execute('DELETE FROM Wednesday WHERE ID == ?', (data,))
    base.commit()

async def sqlDeleteThursday(data):
    cursor.execute('DELETE FROM Thursday WHERE ID == ?', (data,))
    base.commit()

async def sqlDeleteFriday(data):
    cursor.execute('DELETE FROM Friday WHERE ID == ?', (data,))
    base.commit()
