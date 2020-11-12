from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


menu = KeyboardButton('Меню')
cart = KeyboardButton('Корзина')
menu_btns = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).row(menu, cart)

add_to_cart1 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add1')
description1 = InlineKeyboardButton(text='подробнее', callback_data='desc1')
btns1 = InlineKeyboardMarkup(row_width=2).row(add_to_cart1, description1)

add_to_cart2 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add2')
description2 = InlineKeyboardButton(text='подробнее', callback_data='desc2')
btns2 = InlineKeyboardMarkup(row_width=2).row(add_to_cart2, description2)

add_to_cart3 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add3')
description3 = InlineKeyboardButton(text='подробнее', callback_data='desc3')
btns3 = InlineKeyboardMarkup(row_width=2).row(add_to_cart3, description3)
