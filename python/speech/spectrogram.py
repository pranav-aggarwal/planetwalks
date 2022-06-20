import os
import matplotlib.pyplot as plt
import speech_recognition as sr
r1=sr.Recognizer()
with sr.Microphone() as mp:
    print("speek")
    audio_fpath = r1.listen(mp)
print(type(audio_fpath))
get = r1.recognize_google(audio_fpath)
print(get)
print(audio_fpath)
import librosa
import librosa.display
import IPython.display as ipd
audio_clips = os.listdir(audio_fpath)
print("No. of .wav files in audio folder = ",len(audio_clips))