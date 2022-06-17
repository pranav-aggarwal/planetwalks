import speech_recognition as sr
r1=sr.Recognizer()
with sr.Microphone() as mp:
    print("speak now")
    audio =r1.listen(mp)
get =r1.recognize_google(audio)
print(get)
