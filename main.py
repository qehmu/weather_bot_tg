import telebot
from telebot import types

bot = telebot.TeleBot('6440666070:AAE6OoKP-aMhsdO4PHCd7Z26AOrK_U0mgUI')
@bot.message_handler(commands='end')
def start(message):
    bot.send_message(message.chat.id, 'Пока что все, это только начало, тем более разработка этого бота заняла минут 20.')
@bot.message_handler(commands=['hru'])
def start(message):
    bot.send_message(message.chat.id, 'Как дела?')
@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message(message.chat.id, 'Здравствуйте👋')
   bot.send_message(message.chat.id, 'Как дела?')
@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'Понятно, а лет вам сколько?')
@bot.message_handler (content_types=['photo', 'video'])
def start(message):
    bot.send_message(message.chat.id, 'Пока что не могу работать с фото и видео, ждите доработки.')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выбери язык!\nChoose language!')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🇬🇧English', callback_data='English'))
    markup.add(types.InlineKeyboardButton('🇷🇺Русский', callback_data='Russian'))
    bot.reply_to(message, 'Im waiting', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'post_post2')
def send_media_callback(call: types.CallbackQuery):
    if call == 'English':
       bot.send_message(call, 'Write the name of the city to find out what the weather is like!')
    if call == 'Russian':
        bot.send_message(call, 'Напиши город, чтобы узнать там погоду!')
bot.infinity_polling()