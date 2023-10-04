import time
import telebot
from telebot import types
bot = telebot.TeleBot('6510615790:AAFlnwhMUD_dNWwVMZ9tor_V9mVdlqHaeM8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Yes, i want quiz.', callback_data='button_pressed')
    item_2 = types.InlineKeyboardButton('No, i dont wanna quiz.', callback_data='button_not_pressed')
    markup.add(item, item_2)
    bot.send_message(message.chat.id, 'Hello, its quiz.')
    bot.send_message(message.chat.id, 'Want to play?', reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == "button_pressed":
            bot.answer_callback_query(message.call.id, "Okay, let`s try!")
            time.sleep(1)
            bot.send_message(message.chat.id, (str), 'What is 5+5?')
@bot.message_handler(func=lambda message="")
def handle_message(message):
    if message.text == '10':
        bot.reply_to(message, (str), 'Correctly, but what is 61+19?')
    elif message.text == '80':
        bot.reply_to(message, (str),'You`re right again!, but what is 923534x0?')
    elif message.text == '0':
        bot.reply_to(message, 'That`s all, thanks a lot for gaming in quiz!')
#@bot.callback_query_handler()
#def callback_handler(message):
 #   markup_2 = types.InlineKeyboardMarkup(row_width=1)
  #  ite_1 = types.InlineKeyboardButton('Yes, its easy', callback_data='button_presse')
   # ite_2 = types.InlineKeyboardButton('No, its has been hard for me...', callback_data='button')
    #markup_2.add(ite_1, ite_2)
#def startt (message):
    #bot.send_message(message, (str), 'You again right, is it easy for you?')
#@bot.callback_query_handler(func=lambda call: True)
#def callback_handlers(call):
   # if call.data == 'button_presse':
       # bot.answer_callback_query(call.chat.id, 'That`s nice!')
#@bot.callback_query_handler(func=lambda call: True)
#def callback (call):
   # if call.data == 'button':
       # bot.send_message(call.from_user.id, 'That`s really sad, go ahead to learn Math!')
        #exit()
bot.infinity_polling()