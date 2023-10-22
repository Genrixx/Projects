#пока что бетка но функций достаточно
#бот помощник, делал сам

import speech_recognition as sr
import random
import time
import webbrowser
import os
import datetime as dt
import requests
import pyttsx3
import math
engine = pyttsx3.init('sapi5')
#погода
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = '34a98e13a16512ce3f1b2a0659676ab5'
city = 'Tula'
def kelvin_to_celsius(kelvin):
    celcius = kelvin - 273.15
    return celcius

url = base_url + 'appid=' + api_key + "&q=" + city
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feel_like_temp_kelvin = response['main']['feels_like']
feel_like_temp_celsius = kelvin_to_celsius(feel_like_temp_kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

micIndex = 0
wildberries = ["найди на вайлдберизе", "вайлдберриз", "валбериз", "найди на валберизе", "найди на валдберризе", "вайлбериз", "wildberries", "найди на wildberries", "валберис"]
weather_commands = ["погода", "какая погода", "какая погода в городе", "погода на улице", "как погодка", "скажи погоду", "расскажи про погоду", "как там погода"]
whatsup_commands = ["как дела", "как настроение", "как жизнь"]
whatsup_replies = ["Все хорошо, сэр", "Чувствую себя замечательно, сэр", "Не болею, сэр)", "Все супер, сэр", "Не жалуюсь, сэр", "Лучше не бывает"]
hi_commands = ["привет", "джарвис", "добрый день", "добрый вечер", "доброе утро", "салам"]
random_commands = ['орел', 'решка']
bye_commands = ["пока", "хватит", "спокойной ночи", "замолчи", "стоп"]
commands_jarvis = ["сколько время", "подскажи время", "время","день недели", "рандом", "ютуб", "открой youtube", "дата", "ищи", "youtube", "ищи в интернете", "найди", "найди в интернете", "выключи компьютер", "выключи пк", "включи стим", "включи steam", "открой стим", "открой steam", "запусти стим", "запусти steam", "роблокс", "запусти роблокс", "roblox", "запусти roblox"]
thanks_commands = ["спасибо", "благодарю", "спасибо большое", "большое спасибо", "благодарен", "спасиб", "огромное спасибо"]
t = time.time()
time = time.localtime(t)
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if name == "default":
        micIndex = index
        break
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index = micIndex) as source:
        print('Слушаю...')
        audio = r.listen(source)

    text = r.recognize_google(audio, language = 'ru-RU')
    text = text.lower()
    print(text)
    #приветствие джарвиса
    for hear_command in hi_commands:
        if text == hear_command and hear_command == hi_commands[0]:
            engine.say("Здравствуйте, сэр")
            engine.runAndWait()
        elif text == hear_command and hear_command == hi_commands[1]:
            engine.say("Слушаю, сэр")
            engine.runAndWait()
        elif text == hear_command and hear_command == hi_commands[2]:
            engine.say("Добрый день, сэр")
            engine.runAndWait()
            
        elif text == hear_command and hear_command == hi_commands[3]:
            engine.say("Добрый вечер, сэр")
            engine.runAndWait()
            
        elif text == hear_command and hear_command == hi_commands[4]:
            engine.say("Доброе утро, сэр")
            engine.runAndWait()
            
        elif text == hear_command and hear_command == hi_commands[5]:
            engine.say("Асаламалейкум, сэр")
            engine.runAndWait()
            
    #прощание джарвиса
    if text == bye_commands[0]:
        engine.say("Досвидания, сэр")
        engine.runAndWait()
        break
    elif text == bye_commands[1]:
        engine.say("Понял, сэр")
        engine.runAndWait()
        break
    elif text == bye_commands[2]:
        engine.say("Приятных снов, сэр")
        engine.runAndWait()
        break
    elif text == bye_commands[3]:
        engine.say("Я вас услышал, сэр")
        engine.runAndWait()
        break
    elif text == bye_commands[4]:
        engine.say("Понял, сэр")
        engine.runAndWait()
        break
    #комманды джарвиса
    if text == commands_jarvis[0] or text == commands_jarvis[1] or text == commands_jarvis[2]:
        engine.say("{0}:{1}".format(time.tm_hour, time.tm_min))
        engine.runAndWait()
    elif text == commands_jarvis[7]:
        if time.tm_mday > 10:
            engine.say("{0}.{1}.{2}".format(time.tm_mday, time.tm_mon, time.tm_year))
            engine.runAndWait()
        elif time.tm_mday < 10:
            engine.say("0{0}.{1}.{2}".format(time.tm_mday, time.tm_mon, time.tm_year))
            engine.runAndWait()
    elif text == commands_jarvis[3] or text == 'какой сегодня день недели':
        if time.tm_wday == 0:
            engine.say("{0}".format('Понедельник, сэр'))
            engine.runAndWait()
        if time.tm_wday == 1:
            engine.say("{0}".format('Вторник, сэр'))
            engine.runAndWait()
        if time.tm_wday == 2:
            engine.say("{0}".format('Среда, сэр'))
            engine.runAndWait()
        if time.tm_wday == 3:
            engine.say("{0}".format('Четверг, сэр'))
            engine.runAndWait()
        if time.tm_wday == 4:
            engine.say("{0}".format('Пятница, сэр'))
            engine.runAndWait()
        if time.tm_wday == 5:
            engine.say("{0}".format('Суббота, сэр'))
            engine.runAndWait()
        if time.tm_wday == 6:
            engine.say("{0}".format('Воскресенье, сэр'))
            engine.runAndWait()
    elif text == commands_jarvis[4]:
        if random.choice(random_commands) == 'решка':
            engine.say("Выпала решка, сэр")
            engine.runAndWait()
        elif random.choice(random_commands) == 'орел':
            engine.say("Выпал орел, сэр")
            engine.runAndWait()

    elif text == commands_jarvis[5] or text == commands_jarvis[9] or text == commands_jarvis[6]:
        engine.say("Выполняю")
        engine.runAndWait()
        webbrowser.open("https://youtube.com")
    
    elif text == commands_jarvis[8]:
        engine.say("Что искать?")
        engine.runAndWait()
        with sr.Microphone(device_index = micIndex) as source_yt:
            audio_yt = r.listen(source_yt)
        text_yt = text.lower()
        text_yt = r.recognize_google(audio_yt, language = 'ru-RU')
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(text_yt))

    elif text == commands_jarvis[10] or text == commands_jarvis[11] or text == commands_jarvis[12] or text == 'ищи в ютюбе' or text == 'ищи в ютюбе' or text == 'найди на ютуби' or text == 'найди на ютюбе':
        engine.say("Что искать сэр?")
        engine.runAndWait()
        with sr.Microphone(device_index = micIndex) as source_ya:
            audio_ya = r.listen(source_ya)
        text_ya = text.lower()
        text_ya = r.recognize_google(audio_ya, language = 'ru-RU')
        webbrowser.open("https://yandex.ru/search/?text=" + str(text_ya))
        

    elif text == commands_jarvis[13] or text == commands_jarvis[14]:
        engine.say("Выключаю")
        engine.runAndWait()
        os.system ('shutdown /s /t 1')
    elif text == commands_jarvis[15] or text == commands_jarvis[16] or text == commands_jarvis[17] or text == commands_jarvis[18] or text == commands_jarvis[19] or text == commands_jarvis[20]:
        engine.say("Выполняю")
        engine.runAndWait()
        os.startfile("D:/Steam/steam.exe")
   #благодарность джарвису
    elif text in thanks_commands:
        engine.say('Всегда к вашим услугам, сэр')
        engine.runAndWait()

    #настроение джарвиса
    elif text in whatsup_commands:
        engine.say(random.choice(whatsup_replies))
        engine.runAndWait()

    #погода
    elif text in weather_commands:
        engine.say(f"Температура в городе {city}: {math.floor(temp_celsius): .2f}градуса, по ощущениям {math.floor(feel_like_temp_celsius): .2f}градусов, влажность воздуха {humidity}%, скорость ветра {math.floor(wind_speed)}метров в секунду")
        engine.runAndWait()
        
    #wildberries
    elif text in wildberries:
        engine.say("Что искать сэр?")
        engine.runAndWait()
        with sr.Microphone(device_index = micIndex) as source_wb:
            audio_wb = r.listen(source_wb)
        text_wb = text.lower()
        text_wb = r.recognize_google(audio_wb, language = 'ru-RU')
        webbrowser.open("https://www.wildberries.ru/catalog/0/search.aspx?search=" + str(text_wb))
      
    elif text == commands_jarvis[21] or text == commands_jarvis[22] or text == commands_jarvis[23] or text == commands_jarvis[24]:
        engine.say('Выполняю')
        engine.runAndWait()
        os.startfile('C:/Users/Андрей/AppData/Local/Roblox/Versions/version-fa72c1b8c0104006/RobloxPlayerLauncher.exe')
      
