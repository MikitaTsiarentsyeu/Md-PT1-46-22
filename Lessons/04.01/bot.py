import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5054780239:AAE4eIPt6Pz0qrVc1E4GUuwwTNge3LpUMc0')

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    bot.send_message(message.chat.id, "hello!")

@bot.message_handler(commands=['update'])
def update_message(message):
    html = urlopen('https://kurs.onliner.by')
    soup = BeautifulSoup(html)
    tag_list = soup.find_all('p', {'class':'value rise'})
    buy = tag_list[0].text
    sell = tag_list[1].text
    bot.send_message(message.chat.id, buy + ", " + sell)

bot.polling()