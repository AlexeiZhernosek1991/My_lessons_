import csv
import random
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
import pars1

storage = MemoryStorage()
bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(filename='log.txt', filemode='a',
                    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


class Me_info(StatesGroup):
    S1 = State()
    S2 = State()


@dp.message_handler(Command('me'), state=None)
async def enter_me_info(message: types.Message):
    if message.chat.id == config.admin:
        await message.answer("Начинаем настройку \n"
                             "1. Укажите ссылку на Ваш профиль")
        await Me_info.S1.set()  # начинает ждать наш ответ, задав состояние Q1


@dp.message_handler(state=Me_info.S1)
async def answer_for_state_S1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Ваша ссылка сохранена \n"
                         "2. Введите текст")
    await Me_info.S2.set()


@dp.message_handler(state=Me_info.S2)
async def answer_for_state_Q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Текст сохранен")
    data = await state.get_data()
    # достаем значение по ключу answer1
    answer1 = data.get("answer1")
    # достаем значение по ключу answer2
    answer2 = data.get("answer2")
    # открываем файл link.txt на режим записи в кодировке UTF-8
    with open("link.txt", 'w', encoding="UTF-8") as link_txt:
        # записываем строкой ссылку в наш файл
        link_txt.write(str(answer1))
    # открываем файл text.txt в режиме записи в той же кодировке
    with open("text.txt", "w", encoding="UTF-8") as text_txt:
        # записываем в файл текст, который передал пользователь
        text_txt.write(str(answer2))
    # говорим боту отправить сообщение
    await message.answer(f"Ваша ссылка на профиль: {answer1} \n"
                         f"Ваш текст: {answer2}")
    # закрываем текущее состояние
    await state.finish()

class Pars(StatesGroup):
    P1 = State()
@dp.message_handler(Command('pars'), state=None)
async def enter_pars(message: types.Message):
        await message.answer("Начинаем парсинг \n"
                             "Укажите количество страниц")
        await Pars.P1.set()


@dp.message_handler(state=Pars.P1)
async def answer_for_state_P1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer(f"Спарсить {answer} страниц")
    data = await state.get_data()
    answer1 = data.get("answer1")
    pars1.main(answer1)
    await message.answer("Парсинг закончен")
    await bot.send_document(chat_id=message.chat.id, document=open('pars.csv', 'rb'))


@dp.message_handler(Command('start'), start=None)
async def welcome(message):
    joinedFile = open('User.txt', 'r')
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open('User.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f'Привет, *{message.from_user.first_name},* БОТ РАБОТАЕТ',
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(commands=['rassilka'])
async def rassilka(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась* "
                                                f"\nБот оповестит когда рассылку закончите", parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open('User.txt', 'r')
        joinedUsers = set()
        for line in joinedFile:
            joinedUsers.add(line.strip())
        joinedFile.close()
        for user in joinedUsers:
            try:
                await bot.send_photo(user, open('photo.jpg.jpg', 'rb'), message.text[message.text.find(' '):])
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f'*Рассылка Была завершена *\n'
                                                f'получили сообщение: *{receive_users}*\n'
                                                f'заблакировали бота: *{block_users}*', parse_mode='Markdown')


@dp.message_handler(commands="info")
async def cmd_test1(message: types.Message):
    await message.reply("this Bot for learn...")


@dp.message_handler(commands='hellow')
async def cmd_test2(message: types.Message):
    await message.answer('Ссылки', reply_markup=keyboard.hellow)


@dp.message_handler(content_types=['photo'])
async def cmd_test33(message: types.Message):
    a = message.photo[-1].file_id
    await message.photo[-1].download(destination=f'D:\Пайтон\pyproject\practic\Alex12345\Photo\{a}.jpg')
    await bot.send_message(message.chat.id, text='Фотография получена и сохранена\n '
                                                 'Если хотите добавить еще картинку перетащите ее на экран',
                           parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def cmd_test4(message: types.Message):
    if message.text == 'Информация':
        await bot.send_message(message.chat.id, text='Информация \n бот для обучения', parse_mode='Markdown')
    if message.text == 'Статистика':
        await bot.send_message(message.chat.id, text='Статистика \n Cтатистика работы твоего бота в "log.txt"',
                               reply_markup=keyboard.stats, parse_mode='Markdown')
    if message.text == 'Разработчик':
        await bot.send_message(message.chat.id, text='Разработчик \n Выводится информация о разработчике',
                               reply_markup=keyboard.developer, parse_mode='Markdown')
    if message.text == 'Покажи пользователя':
        await bot.send_message(message.chat.id, text='Вы хотите получить информацию о своем ID',
                               reply_markup=keyboard.show_user, parse_mode='Markdown')
    if message.text == 'Отправить фото':
        await bot.send_photo(message.chat.id, open(f'Photo\\{random.randint(2, 4)}.jpg', 'rb'))


@dp.callback_query_handler(text_contains='join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('User.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'У тебя нет админки\n куда ты полез', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Ты вернулся на главное меню. Жми опять кнопки', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='id')
async def id_(call: types.CallbackQuery):
    a = str(call.message.chat.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'Ваш id:{a} ', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='no')
async def no_(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Вы вернулись на главное меню', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='x')
async def no_1(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Вы отменили выбор', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='yes')
async def yes_(call: types.CallbackQuery):
    joinedlink = open('link.txt', encoding='utf8')
    link_string = joinedlink.read()
    joinedtext = open('text.txt', encoding='utf8')
    text_string = joinedtext.read()
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"Профиль разработчика: {link_string} \n"
                                     f"Коментарий: {text_string}", parse_mode='Markdown')
    joinedlink.close()
    joinedtext.close()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
