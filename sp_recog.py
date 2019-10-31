# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 00:14:01 2019

@author: Satvik Chachra
"""
import speech_recognition as sr
AUDIO_FILE=("name_of_file.wav")
#initialize the recognizer
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    #reads audio file
    audio = r.record(source)
    
try:
    #convert audio to text
    print("audio file contains : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("google speech recognition could not understand audio")
except sr.RequestError:
    print("couldn't get results from google speech recognition")
     
    
import speech_recognition as sr
