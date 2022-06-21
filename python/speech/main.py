import speech_recognition as sr
import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import librosa
import librosa.display

#to play audio
import IPython.display as ipd
r1=sr.Recognizer()
with sr.Microphone() as mp:
    print("speak now")
    audio =r1.listen(mp)
librosa.display.waveplot(audio)
get =r1.recognize_google(audio)
print(get)
