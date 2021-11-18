# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 01:18:59 2021

@author: SHARATH
"""

import datetime
import winsound
import pyttsx3

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    
    altime = altime[11:-3]
    
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")
    engine = pyttsx3.init()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    while True:
        if Horeal == datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Boss wakeup")
                speak("Boss wakeup")
                winsound.PlaySound('abc', winsound.SND_LOOP)
                
            elif Mireal<datetime.datetime.now().minute:
                break
            