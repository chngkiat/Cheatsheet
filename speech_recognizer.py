# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:49:18 2021

@author: chng_
"""
import speech_recognition as sr 
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)