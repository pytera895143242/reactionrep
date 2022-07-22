from aiogram import types
from misc import dp,bot
import asyncio
from .callbak_data import akkaunts

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID = [ADMIN_ID_1,ADMIN_ID_2]

flag1 = 1 #НАСТРОЙКА РЕЖИМА ПОКАЗА FILE ID

@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    t = message.text.split(" - ")
    await akkaunts(t[0],t[1])