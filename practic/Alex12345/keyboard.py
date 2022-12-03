from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

info = types.KeyboardButton('Информация')
stats = types.KeyboardButton('Статистика')
developer = types.KeyboardButton('Разработчик')
show_user = types.KeyboardButton('Покажи пользователя')
photo = types.KeyboardButton('Отправить фото')

start.add(stats, info, developer, show_user, photo)

hellow = types.InlineKeyboardMarkup(row_width=1)

i = types.InlineKeyboardButton(text='ссылка1', url='https://av.by/')
s = types.InlineKeyboardButton(text='ссылка2', url='https://www.youtube.com/')

hellow.add(i, s)

stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton('Yes', callback_data='join'))
stats.add(InlineKeyboardButton('Now', callback_data='cancle'))

developer = InlineKeyboardMarkup()
developer.add(InlineKeyboardButton('Yes', callback_data='yes'))
developer.add(InlineKeyboardButton('No', callback_data='no'))

show_user = InlineKeyboardMarkup()
show_user.add(InlineKeyboardButton('Хочу видеть id', callback_data='id'))
show_user.add(InlineKeyboardButton('Вернуться обратно', callback_data='x'))

# photo = InlineKeyboardMarkup()
# photo.add(InlineKeyboardButton('Показать все загруженные фото', callback_data='photo'))
# photo.add(InlineKeyboardButton('Показать все загруженные фото', callback_data='not'))