import config
import telebot
from telebot import types
import shelve
import random
import requests
import os
token = os.environ["token"]

bot = telebot.TeleBot(token)

from html.parser import HTMLParser
from html.entities import name2codepoint

class Html(HTMLParser):
    url = ""
    def handle_starttag(self, tag, attrs):
        t = 0
        for attr in attrs:
            if "data-large-file-url" in attr:
                if "https" in attr[1]:
                    self.url = attr[1]
                else:
                    self.url = "https://danbooru.donmai.us/" + attr[1]




html = Html()


bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def mess(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Аніме', 'Вихід')
   # markup.row("Розклад", "Записати розклад")
    bot.send_message(message.chat.id, "Погнали", reply_markup=markup)


@bot.message_handler(regexp="Вихід")
def mess(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text="ok", reply_markup=markup)

@bot.message_handler(regexp="Новатор запиши")
def messs(message):
    #bot.send_message(message.chat.id, message.text)
    with shelve.open("dict.txt") as file:
        for i in file.keys():
            if i in message.text:
                file[i] = message.text


@bot.message_handler(regexp="розклад")
def mess(message):
    #bot.send_message(message.chat.id, message.text)
    text = ""
    with shelve.open("dict.txt") as file:
        for i in file.keys():
            text += "**{}** \n{}".format(i, file[i])
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["pidor", "help"])
def mess(message):
    bot.send_message(message.chat.id, "{}, ти підор".format(message.chat.first_name))



@bot.message_handler(regexp="Аніме")
def mess(message):
    r = requests.get("https://danbooru.donmai.us/posts/"+str(random.randrange(3035774)))
    html.feed(r.text)
    p = requests.get(html.url)
    bot.send_photo(message.chat.id, p.content)



if __name__ == "__main__":
    bot.polling(none_stop=True)
