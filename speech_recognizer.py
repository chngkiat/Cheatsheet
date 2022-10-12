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
    print ('Start Speaking')
    audio_data = r.record(source, duration=10)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)

import cv2

vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()