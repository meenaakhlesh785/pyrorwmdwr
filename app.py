import os
from flask import Flask,render_template,request,redirect
import telebot
import logging
import os
import pyrogram
from pyrogram import Client
 
 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
 


TOKEN = '2109918986:AAE8KJ6Zvj0mmJxayX-fusTFWZ2fzm56EHA'
API_ID = 1774230
API_HASH = "b0829cf5b62052d6c8adee27b02f1f00"
#bot = telebot.TeleBot(TOKEN)
#app=Flask(__name__)
server = Flask(__name__)


#@bot.message_handler(commands=['start'])
def#def start(message):
    #bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == "__main__":
  #threading.Thread(target=runAutoList, name='run_server_time', daemon=True).start()
  #server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
  #server.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
  server.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 1000)))
 

#if __name__=='__main__':
    #app.run(debug=True)
