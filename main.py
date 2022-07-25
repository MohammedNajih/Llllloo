import requests,user_agent,json,flask,telebot,random,os,sys
import telebot 
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
from telebot import TeleBot,types
import time
from gdolib import *

bot = telebot.TeleBot(BOT_TOKEN)

server = Flask(__name__)

logger = telebot.logger

logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text="بوت لعرض ايدي البوست")
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=" ارسل الرابط الان")

@bot.message_handler(content_types = ['text'])
def basha(m):
 ba = m.text 
 id = gdo_drow.id_post(ba)
 bot.send_message(m.chat.id,text=id)

def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://zonyo.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
