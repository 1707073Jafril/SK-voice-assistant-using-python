import speech_recognition as spr
for index, name in enumerate(spr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

import pyttsx3
import pyaudio
import webbrowser
import datetime
import wikipedia
import time
import pywhatkit
import wolframalpha
import os
import cv2
import pyautogui
import requests
import bs4
import pandas
from ecapture import ecapture as ec
from pyowm import OWM
import re
import sys
import numpy as np




shihab = pyttsx3.init('sapi5')
voices = shihab.getProperty('voices')
shihab.setProperty('voice', voices[0].id)

def intro():
    hour = int(datetime.datetime.now().hour)
    if (hour != 0):
        reply("Assalamu Alaikum ! I am SK voice assistant , I am waiting to help you!")

def reply(text):
    shihab.say(text)
    shihab.runAndWait()

#def Hello():
   # reply("Hello ! Shihab Sir , Assalamu Alaikum")

def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 10:
        greeting = 'Good morning , shihab!'
    elif hour >= 10 and hour < 15:
        greeting = 'Good afternoon!'
    elif hour >= 18 and hour < 5:
        greeting = 'Good night'
    else:
        greeting = 'Good evening!'
    reply(greeting)


def order():
    global command
    listener = spr.Recognizer()
    with spr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('I am listening...')
        reply('I am listening!!')
        voice = listener.listen(source)

    try:
        #command = None  # (<-- !!!)
        command = listener.recognize_google(voice)
        print(command)
        if 'shihab' in command:
            command = command.replace('shihab', '')

    except Exception as e:
                    print("Try again , sir!")
                    pass
    return command


def msk():
    command = order()

    if 'hello' in command:
        a=command.replace('hello' , '')
        reply("Hi , How are you? I am waiting for your order")
        time.sleep(3)

    elif 'about you' in command:
        reply('Assalamu Alaikum. I am SK voice assistant and I was developed by Md. Jafril Alam Shihab.He is a student of CSE of Khulna University of Engineering and Technology. My features are awesome!')
        time.sleep(2)

    elif ('my friend') in command:
        reply("What is the name of your friend")
        name1 = order()
        reply('welcome and best wishes Mr ' + name1)
        time.sleep(3)

    elif 'SK' in command:
        #a=command.replace('hello' , '')
        reply("Lots of love for you!!")
        time.sleep(2)

    elif 'infopedia' in command:
        reply('Sir , Ask me any question.')
        ask = order()
        app_id = "EVEEQL-J3RQPHTQ8W"
        client = wolframalpha.Client('EVEEQL-J3RQPHTQ8W')
        result = client.query(ask)
        answer = next(result.results).text
        print(answer)
        reply(answer)
        time.sleep(3)

    elif 'time' in command:
        a = command.replace('time','')
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        reply(f"the time is {strTime}")
        time.sleep(3)

    elif 'play' in command:
        song = command.replace('play', '')
        reply('playing ' + song)
        pywhatkit.playonyt(song)
        time.sleep(3)

    elif 'play movie' in command:
        movie = command.replace('play movie', '')
        reply('playing ' + movie)
        pywhatkit.playonyt(movie)
        time.sleep(3)

    elif 'map' in command:
        content = command.replace('map', '')
        url = 'https://www.google.com/maps/place/' + content + '/&amp'
        webbrowser.get().open(url)
        reply(content)
        time.sleep(3)


    elif 'shut up' in command:
        command.replace('shut up','')
        reply("Good bye , Md. Jafril Alam shihab ! You are welcomed ")
        exit()

    elif 'search' in command:
        content = command.replace('Google search' , '')
        reply('Searching your content , wait' + content)
        url = 'https://www.google.com/search?q=' + content
        webbrowser.get().open(url)
        reply("Your result has found!")
        time.sleep(3)


    elif 'open browser' in command:
        command.replace('open browser', '')
        reply('Opening our browser ')
        webbrowser.open('https://www.google.com.bd/')
        webbrowser.get('mozilla')
        time.sleep(3)

    elif 'camera' in command:
        print("Sir ,Camera is opening!")
        reply("Sir ,Camera is opening!")
        reply("Sir ,What is the file name?")
        name = order()
        img = cv2.VideoCapture(0)
        image = img.read()[1]
        #display = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera",image)
        if cv2.waitKey(0) == ord('s'):
            cv2.imwrite(f"{name}.jpg",image)
        cv2.destroyAllWindows()
        time.sleep(3)


    elif 'videocamera' in command:
        print("Sir ,video Camera is opening!")
        reply("Sir ,video Camera is opening!")
        #reply("Sir , say name of the file ")
        #name = order()
        img = cv2.VideoCapture(0)
        while (True):
            ret , frame = img.read()
            shot = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', shot)
            if cv2.waitKey(1) == ord('s'):
                #cv2.imwrite(f"{name}.png",img)
                break
        img.release()
        cv2.destroyAllWindows()
        time.sleep(3)

    elif 'screenshot' in command:
        reply("And the file name would be...")
        name = order()
        p=pyautogui.screenshot(f"desktop{name}.png")
        reply("The screenshot has captured!!")
        #ss.save(r"C:\Users\asus\Pictures\Saved Pictures\{name}.png")
        #os.startfile(r"C:\Users\asus\PycharmProjects\SK_assistant\venv\{name}")
        time.sleep(3)

    elif 'weather of' in command:
        city = command.replace('weather of', '')
        owm = OWM(API_key='170f3e42dec9a08a4ea288e533ca533c')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        w_status = w.get_status()
        w_t = w.get_temperature(unit='celsius')
        w_wi = w.get_wind()
        w_humidity = w.get_humidity()
        w_cld = w.get_clouds()
        print('Weather of %s is %s . Temperature is %0.4f . Wind speed is %0.2f and humidity is %0.2f percent and cloud is %d' % (city, w_status, w_t['temp'], w_wi['speed'], w_humidity,w_cld))
        reply('Weather of %s is %s . Temperature is %0.4f . Wind speed is %0.2f and humidity is %0.2f percent and cloud is %d' % (city, w_status, w_t['temp'], w_wi['speed'], w_humidity,w_cld))
        time.sleep(3)

    elif 'when did' in command or 'what is ' or 'what do' or 'what does' or 'what did' or 'what are' or 'who is ' or 'who are' or 'who does' or 'who did' or 'where is ' or 'where are' or 'where do' or 'where does' or 'where did' or 'when do' or 'when does' in command or ('wikipedia' in command):
        reply('Searching Wikipedia...')
        output = command.replace('wikipedia', '')
        output = command.replace('what is', '')
        output = command.replace('what are', '')
        output = command.replace('what do', '')
        output = command.replace('what did', '')
        output = command.replace('what does', '')
        output = command.replace('who is', '')
        output = command.replace('who are', '')
        output = command.replace('who does', '')
        output = command.replace('who did', '')
        output = command.replace('where is', '')
        output = command.replace('where are', '')
        output = command.replace('where do', '')
        output = command.replace('where does', '')
        output = command.replace('where did', '')
        output = command.replace('when do', '')
        output = command.replace('when does', '')
        output = command.replace('when did', '')
        search_results = wikipedia.summary(output, 10)
        print(search_results)
        reply(search_results)
        time.sleep(3)

    else:
        reply('Ups !! Cannot finding it')
        pywhatkit.search(command)


#Hello()
intro()
Greetings()
while True:
    msk()
time.sleep(10)