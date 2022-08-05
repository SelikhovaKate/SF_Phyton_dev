import telebot
from extensions import APIException, CurrenciesConverter
from config import TOKEN, exchanges
import traceback

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message:telebot.types.Message):
    msg = 'Вам денег поменять или поговорить? Если поменять, то от вас надо: _<какую валюту продаем> <какую валюту покупаем> <сколько денег у вас есть?>_. \n \
Меняем почти все, если хотите знать что именно, введите: /values.'
    bot.reply_to(message, msg, parse_mode='Markdown')

# Обрабатывается сообщение с командой '/values'.
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Что мы имеем вам предложить:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

# Обрабатываются команды конвертации
@bot.message_handler(content_types=['text'])
def handle_convert(message):
    try:
        values = message.text.split(' ')
        if len(values) < 3:
            raise APIException('что-то вы скрываете, не все указали')

        if len(values) > 3:
            raise APIException('зачем нам лишнее знать, оно нам не надо')

        msg = CurrenciesConverter.convert(values)
    except APIException as e:
        bot.reply_to(message, f'Неверная команда боту.\n_{e}_', parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n_{e}_', parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, msg, parse_mode='Markdown')


bot.polling(none_stop=True)