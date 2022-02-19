from telebot import types


def buttons_lst(lst):
    ls = []
    for item in lst:
        btn = types.KeyboardButton(item)
        ls.append(btn)
    return ls


def buttons(dct):
    ls = []
    for k, v in dct.items():
        urls = types.InlineKeyboardButton(k, url=v)
        ls.append(urls)
    return ls


