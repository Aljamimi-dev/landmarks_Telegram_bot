from telebot import TeleBot
from api import get_gpt_reply


bot_token = TeleBot('Enter your telegram bot token')

# The reply when the user press start (Listener for the bot start)
@bot_token.message_handler(commands=['start'])
def on_start(message):
    chat_id = message.chat.id
    bot_token.send_message(chat_id, 'Hello, please write the country/city name')
    return

# Listener for the user message to get the reply from chagpt
@bot_token.message_handler()
def on_message(message):
    chat_id = message.chat.id
    prompt = message.text
    bot_token.send_chat_action(chat_id, action='typing')
    bot_token.send_message(chat_id, get_gpt_reply(prompt))
    return


bot_token.infinity_polling()

