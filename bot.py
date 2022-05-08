from telebot import TeleBot, types

from parser import weather, money_rate

token = ''

bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather_button = types.KeyboardButton('Погода')
    money_button = types.KeyboardButton('Курс валют')
    keyboard.add(weather_button, money_button)
    bot.send_message(message.chat.id, 'Выберите опцию', reply_markup=keyboard)

@bot.message_handler(regexp='Погода')
def send_weather(message):
    weather_info = weather()
    bot.send_message(
        message.chat.id, 
        weather_info, 
    )

@bot.message_handler(regexp='Курс валют')
def send_money_info(message):
    money_info = money_rate()
    bot.send_message(
        message.chat.id, 
        money_info, 
    )

bot.polling()
