#мой тг бот для новостей с хабра, сыроват
import telebot
import requests
from bs4 import BeautifulSoup
import time


token = '6325769979:AAF-hs9clh6FKOsJ_zOK3DP57FOTORA-4lw'
id_chanel = '@itshkaaaa'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def commands(message):
    if message.text == "Старт":
        post_text = parser()
        bot.send_message(id_chanel, post_text)        
            
def parser():
    url = "https://habr.com/ru/search/?q=python&target_type=posts&order=relevance"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find('h2', class_='tm-title tm-title_h2')
    post_time = soup.find('span', class_='tm-article-reading-time__label')
    source = soup.find('a', class_='tm-title__link', href=True)
    return (post.text + 'Время для прочтения ' + post_time.text + 'Ссылка - https://habr.com'+ source['href'])

    


bot.polling()
