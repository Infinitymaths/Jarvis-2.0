# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:21:03 2021

@author: SHARATH
"""

import pyttsx3  # importing the module. This module converts text data into speech
import datetime
import speech_recognition as sr
import smtplib
from secret import sender_email, epwd #self made
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi.newsapi_client import NewsApiClient
import clipboard
import os
import pyjokes
import string
import random
import psutil
# from nltk.tokenize import word_tokenize
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisgui_1 import Ui_MainWindow
import sys
import operator
from pywikihow import search_wikihow
import cv2
import MyAlarm #self made
from face_recognition import recognition #self made
from nltk_module import extract_names
from phonebook import phone_numbers,email_address
import locationtagger
from volume_control import volume_control


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoice(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello boss this is jarvis")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello boss this is friday")


def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is:- ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is :- ")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("good evening sir")
    else:
        speak("Boss go and sleep... and let me rest boss..")


def wishme():
    # speak("Hello sir!!")
    greeting()
    # date()
    # time()
    # if (engine.getProperty(
    #         'voice') == 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'):
    #     speak("Jarvis at your service!!! How can i help you")
    # else:
    #     speak("Friday at your service! How can i help you")


# def takecommandCMD():
#     query = input("Please tell me how can i help you?")
#     return query



def sendemail(receiver, subject,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, epwd)
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(msg)
    server.send_message(email)
    # server.sendmail(sender_email, 'priyankakadam6805@gmail.com', msg)
    server.close()


def sendwhatsmsg(phone_number, message):
    Message = message
    number = phone_number
    wb.open('https://web.whatsapp.com/send?phone=' + number + '&text=' + Message)
    sleep(20)
    pyautogui.click(x=869, y=966)
    pyautogui.click(button='left')
    pyautogui.press('enter')


def searchgoogle(search):
    wb.open('https://www.google.com/search?q=' + search)


# https://api.openweathermap.org/data/2.5/weather?q={City Name}&units=imperial&appid={e3dbb09688459d7411f7cfc5d483f437}
def news(name,category):
    countr_list = {
        'india': 'in',
        'uae': 'ae',
        'usa': 'us'

    }
    country = countr_list[name]
    newsapi = NewsApiClient(api_key='db5836083045489ca54a668c30fafa9b')
    data = newsapi.get_top_headlines(q=category,
                                     language='en',
                                     page_size=5,
                                     country=country)
    newsdata = data['articles']
    speak("here is your news boss")
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')

    speak("that's it for now I'll update you in some time")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def covid():
    req = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = req.json()
    covid_data = f'Confirmed cases: {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered: {data["recovered"]}'

    print(covid_data)
    speak(covid_data)


def screenshot():
    name_img = datetime.datetime.now().strftime("%Y%B%d-%H%M%S")
    name_img = str(name_img)
    name_img = 'screenshots\\{}.png'.format(name_img)
    img = pyautogui.screenshot(name_img)
    img.show()


def password_generator(n):
    string1 = string.ascii_uppercase
    string2 = string.ascii_lowercase
    string3 = string.digits
    string4 = string.punctuation

    speak("tell me the length of the password")
    try:
        raw_length = int(n)
    except:
        speak("Sorry boss try again")
        password_generator()

    if raw_length >= 5 and raw_length <= 16:
        length = raw_length
    else:
        speak("sorry boss length is too small or too long")
        password_generator()

    s = []
    s.extend(list(string1))
    s.extend(list(string2))
    s.extend(list(string3))
    s.extend(list(string4))

    random.shuffle(s)
    newpass = ("".join(s[0:length]))
    print(newpass)
    speak(newpass)


def flip():
    speak("Flipping a coin boss")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)

    toss = ("".join(toss[0]))
    print("Boss after flipping you got " + toss)
    speak("Boss after flipping you got " + toss)


def roll():
    speak("Rolling a die boss")
    die = ['1', '2', '3', '4', '5', '6']
    ans = []
    ans.extend(die)
    random.shuffle(ans)

    ans = ("".join(ans[0]))
    print("Boss after rolling you got " + ans)
    speak("Boss after rolling you got " + ans)

def calculations():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what do you want to calculate, like 3 plus 3")
        print("listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)
    def get_operator(op):
        return {
            '+' : operator.add,
            '-' : operator.sub,
            'X' : operator.mul,
            'divided' : operator.__truediv__,
            }[op]
    def eval_binary_expr(op1,oper,op2):
        try:
            op1,op2 = int(op1),int(op2)
            return get_operator(oper)(op1,op2)
        except:
            speak("boss there is some problem in inputs")
            calculations()
    ans =  eval_binary_expr(*(my_string.split()))      
    speak("your result is")
    speak(ans)
    print("your result is")
    print(ans)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("Boss your systems cpu usage is " + usage)
    battery = psutil.sensors_battery()
    speak("and the battery is ")
    speak(battery.percent)

class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self):
        while True:
            ans = recognition()
            if ans==True:
                while True:
                    permission = self.takecommandMic().lower()
                    if 'jarvis' in permission:
                        print(permission)
                        getvoice(1)
                        self.taskexecution()
                    elif 'friday' in permission:
                        print(permission)
                        getvoice(2)
                        self.taskexecution()
                    elif 'bye' in permission or 'good bye' in permission or 'goodbye' in permission or 'offline' in permission:
                        sys.exit()
            
           
    
    def takecommandMic(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            # print(query)
    
        except Exception as e:
            print(e)
            # speak("Say it again")
            return "None"
        return query
    
    def taskexecution(self):   
        # main = Phonebook()
        wishme()
        # wakeword1 = 'jarvis'
        # wakeword2 =  'friday'
        while True:
            self.query = self.takecommandMic().lower()
            # self.query = word_tokenize(self.query)
            print(self.query)
    
            # if True:
            if 'time' in self.query:
                time()
            elif 'date' in self.query:
                date()
            elif 'call friday' in self.query:
                getvoice(2)
            elif 'call jarvis' in self.query:
                getvoice(1)
            elif 'send email' in self.query:
                # email_list = {
                #     'testemail': 'sharath.p@somaiya.edu',
                #     'priyanka': 'priyankakadam6805@gmail.com',
                #     'siddhi': 'siddhisurve786@gmail.con'
                # }
                try:
                    speak("Email id of the receiver boss")
                    name = self.takecommandMic().lower()
                    receiver = email_address(name)
                    speak("tell me the subject boss")
                    subject = self.takecommandMic()
                    speak("Tell me the message boss")
                    msg = self.takecommandMic().lower()
                    sendemail(receiver, subject,msg)
                    speak("email send boss..")
                except Exception as e:
                    print(e)
                    print("unable to send email")
                    speak("say it again")
            elif 'message' in self.query:
                # user_name = {
                #     'number': '+91 93593 21553'
                # }
                try:
                    speak("whom should i send the message boss")
                    name = self.takecommandMic().lower()
                    print(name)
                    phone_number = phone_numbers(name)
                    speak("What is the message boss?")
                    message = self.takecommandMic()
                    print(message)
                    sendwhatsmsg(phone_number, message)
                    speak("Message sent boss")
                except Exception as e:
                    print(e)
                    speak("Unable to send message boss")
        
            elif 'wikipedia' in self.query:
                speak("searching....")
                self.query = self.query.replace('wikipedia', "")
                result = wikipedia.summary(self.query, sentences=2)
                print(result)
                speak(result)
            elif 'alarm' in self.query:
                speak("boss please tell me the time to set alarm. For example, set alarm to 5:30 a.m.")
                tt = self.takecommandMic().lower()
                tt = tt.replace("set alarm to ","") 
                tt = tt.replace(".","")
                tt = tt.upper()
                MyAlarm.alarm(tt)
                comm = self.takecommandMic().lower()
                if 'woked up' in comm or 'jarvis just waked up' in comm:
                    speak("good boss... Now you can continue your work")
                elif 'just' in comm:
                    speak("boss you better wake up or you will receive a flying sandal")
            elif 'google' in self.query:
                speak("what should i search in google boss")
                search = self.takecommandMic()
                searchgoogle(search)
            elif 'shutdown' in self.query:
                os.system("shutdown /s /t S")
            elif 'restart' in self.query:
                os.system('shutdown /r /t S')
            elif 'sleep' in self.query and 'computer' in self.query:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            elif 'youtube' in self.query:
                speak("what should i search boss")
                topic = self.takecommandMic()
                pywhatkit.playonyt(topic)
    
            elif 'weather' in self.query:
                speak("Which city boss")
                city = self.takecommandMic().lower()
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=e3dbb09688459d7411f7cfc5d483f437'
                res = requests.get(url)
                data = res.json()
    
                weather = data['weather'][0]['main']
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                temp = round((temperature - 32) * 5 / 9)
                print(weather)
                print(temp)
                print(description)
                speak(f'boss weather in {city} is' + description)
                speak("and the temperature is {} degree celcius".format(temp))
    
            elif 'news' in self.query:
                speak("which country sir")
                name = self.takecommandMic().lower()
                place_entity = locationtagger.find_locations(text = name)
                name = place_entity.countries[0]
                speak("which category boss")
                category = self.takecommandMic().lower()
                news(name,category)
    
            elif 'read the text' in self.query:
                text2speech()
    
            elif 'covid' in self.query:
                covid()
            elif 'open' in self.query:
                os.system('explorer C://{}'.format(self.query.replace('open', '')))
    
            elif 'open brave' in self.query:
                codepath = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
                os.startfile(codepath)
            elif 'open spyder' in self.query:
                codepath = 'C:\\Users\\SHARATH\\anaconda3\\pythonw.exe'
                os.startfile(codepath)
            elif 'open pycharm' in self.query:
                codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe'
                os.startfile(codepath)
            elif 'open table' in self.query:
                codepath = 'C:\\Program Files\\Tableau\\Tableau Public 2021.3\\bin\\tabpublic.exe'
                os.startfile(codepath)
    
            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
    
            elif 'screenshot' in self.query:
                screenshot()
            elif 'activate how to do protocol' in self.query:
                speak("Protocol initiated boss..")
                while True:
                    speak("Sir what is the command:-")
                    how = self.takecommandMic().lower()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay sir.. Protocol is deactivated..")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how,max_results)
                            assert len(how_to)==1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception:
                        speak("Sorry sir, i am not able to find this..")
            elif 'remember' in self.query:
                speak("What should i remember boss")
                data = self.takecommandMic()
                speak("you said me to remember that " + data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
    
            elif 'anything' in self.query:
                remember = open('data.txt', 'r')
                if os.path.getsize('data.txt') == 0:
                    speak("No boss i don't know anything")
                else:
                    speak("you told me to remember that " + remember.read())
                
            elif 'open camera' in self.query or 'selfie' in self.query:
                name_img = datetime.datetime.now().strftime("%Y%B%d-%H%M%S")
                name_img = str(name_img)
                name_img = 'cameraimages\\{}.png'.format(name_img)
                cap = cv2.VideoCapture(0)
                while True:
                    ret,img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                    cv2.imwrite(name_img,img)
                    cap.release()
                    cv2.destroyAllWindows()
            elif 'volume control' in self.query:
                volume_control()
                
            elif 'volume up' in self.query:
                pyautogui.press('volumeup')
            
            elif 'volume down' in self.query:
                pyautogui.press('volumedown')
            
            elif 'volume mute' in self.query or 'mute' in self.query:
                pyautogui.press('volumemute')
            
            elif 'password' in self.query:
                speak("Tell me the length of the password boss")
                n = self.takecommandMic()
                password_generator(n)
            elif 'flip a coin' in self.query:
                flip()
    
            elif 'roll a die' in self.query:
                roll()
    
            elif 'cpu usage' in self.query:
                cpu()
            elif 'find my location' in self.query or 'trace my location' in self.query:
                speak("yes boss checking the location...")
                try:
                    ipadd = requests.get('https://api.ipify.org').text
                    print(ipadd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir i think you are in {city} city located in {country}")
                    print(f"Sir i think you are in {city} city located in {country}")
                except Exception:
                    speak("Sorry sir i am not able to locate. i guess there is some network issue...")
            elif "do calculation" in self.query or "can you perform calculations" in self.query:
                calculations()
            elif 'hello' in self.query or 'hey' in self.query:
                speak("hello boss, how may i help you")
            elif 'how are you' in self.query:
                speak("I am fine sir. What about you boss.")
            elif 'also good' in self.query or 'fine' in self.query:
                speak("that's great boss...")
            elif 'not good' in self.query or 'not fine' in self.query:
                speak("What happened sir... any problem boss... is your girlfriend mad at you boss..")
            elif 'naughty jarvis' in self.query or 'naughty friday' in self.query:
                speak("Studied from you boss.")
            elif 'thank you' in self.query or 'thanks' in self.query:
                speak("always at your service boss")
            elif 'jarvis good morning' in self.query or 'jarvis good afternoon' in self.query or 'jarvis good evening' in self.query or 'jarvis good night' in self.query:
                command = self.query.replace('jarvis','')
                speak(f"{command} boss")
            elif 'good morning jarvis' in self.query or 'good afternoon jarvis' in self.query or 'good evening jarvis' in self.query or 'good night jarvis' in self.query:
                command = self.query.replace('jarvis','')
                speak(f"{command} boss")
            elif 'friday good morning' in self.query or 'friday good afternoon' in self.query or 'friday good evening' in self.query or 'friday good night' in self.query:
                command = self.query.replace('friday','')
                speak(f"{command} boss")
            elif 'good morning friday' in self.query or 'good afternoon friday' in self.query or 'good evening friday' in self.query or 'good night friday' in self.query:
                command = self.query.replace('friday','')
                speak(f"{command} boss")
            elif 'who is here' in self.query:
                speak("Who is here boss.. Anyone special")
                name = self.takecommandMic().lower()
                final_name = extract_names(name)
                final_name = final_name.remove('jarvis')
                final_name = final_name.remove('friday')
                for element in final_name:
                    speak("Hey {}".format(element))
                speak("how are you")
                self.query = self.takecommandMic().lower()
                if 'hello' in self.query or 'hey' in self.query:
                    speak("hello boss, how may i help you")
                elif 'how are you' in self.query:
                    speak("I am fine sir. What about you boss.")
                elif 'also good' in self.query or 'fine' in self.query:
                    speak("that's great boss...")
                elif 'not good' in self.query or 'not fine' in self.query:
                    speak("What happened buddy... any problem ... did mom scolded for something..")
            elif 'go to sleep' in self.query:
                speak("Boss do you really think i should go to sleep..")
                option = self.takecommandMic().lower()
                if option == 'yes' or option == 'yep':
                    speak("bye bye boss")
                    break
                else:
                    speak("i am listening")
                    pass
            elif 'good bye' in self.query or 'goodbye' in self.query or 'offline' in self.query:
                speak("Good bye boss... Take care boss")
                sys.exit()
                
startExecution = MainThread()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images for GUI/JARVIS AI.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)        
        

app = QtWidgets.QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())