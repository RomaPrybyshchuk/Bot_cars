import telebot
import config
from telebot import types
import info
import make_keyboard


bot = telebot.TeleBot(config.TOKEN)


def markup_buttons(message, description, dict_urls):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(*make_keyboard.buttons(dict_urls))
    bot.send_message(message.chat.id, description, reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    greeting = open('greeting/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, greeting)
    bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>!"
                                      f"\nЯ - <b>{bot.get_me().first_name}</b>, "
                                      "бот который расскажет как купить авто в РБ.",
                                      parse_mode="HTML")
    bot.send_message(message.chat.id, 'Нажми на /help чтобы узнать подробности.')


@bot.message_handler(commands=['help'])
def call_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(*make_keyboard.buttons_lst(info.resources))
    bot.send_message(message.chat.id, "Что тебя интересует: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_buttons(message):
    if message.text == 'Сайты продажи авто в РБ':
        markup_buttons(message, "Самые популярные сайты: ", info.urls_buy_cars)

    elif message.text == 'Фирмы автопригона':
        markup_buttons(message, "Компании по автопригону из Европы и США: ", info.urls_avtoprivoz)

    elif message.text == 'Услуги автоподбора':
        markup_buttons(message, "Фирмы по автоподбору: ", info.urls_avtopodbor)

    elif message.text == 'Дополнительная информация':
        markup_buttons(message, "Немного полезной информации: ", info.extra_info)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю.'
                                          'Я могу только /start и /help.')


if __name__ == "__main__":
    bot.infinity_polling()
