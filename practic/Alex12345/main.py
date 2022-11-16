from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import keyboard
import logging

storage = MemoryStorage()
bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(levelname)-8s [%(asctime)s] %(message)s', filename='log.txt',
                    level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.reply("I'm working, sif!")


@dp.message_handler(commands="info")
async def cmd_test1(message: types.Message):
    await message.reply("this Bot for learn...")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
