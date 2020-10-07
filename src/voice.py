#pip: pywin32, pypiwin32, pyttx3, SpeechRecognition, pipwin, pypiwin, fuzzywuzzy
#pipwin: PyAudio

import pyttsx3 as px
import speech_recognition as sr
from multiprocessing import Pool, freeze_support
#from google import speak_g
from time import sleep

def savewords(my_words):
    try:
        with open("dialog.txt", "r") as f:
            text = f.read()
    except:
        pass
    with open("dialog.txt","w") as f:
        f.write(text+"\n"+str(my_words))

def speak(my_words):
    voice.say(my_words)
    voice.runAndWait()
    voice.stop()

def read(a=0):
    with m as source:
        print("[] Speak...")
        #speak("*")
        audio = r.listen(source, timeout=2, phrase_time_limit=200)
    return r.recognize_google(audio, language="ru-RU").lower()

r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = px.init()

with m as source:
    r.adjust_for_ambient_noise(source)

while True:
    try:
        # with Pool(processes=1) as pool:
        #     my_words = pool.map(read,[], 10)

        my_words = read()
        savewords(my_words)
        print("[] *...")
        print(":", my_words)

        # with Pool(processes=1) as pool:
        #     pool.map(speak, my_words, 10)

        speak(my_words)

        print("[] *...")
    except sr.UnknownValueError:
        print("Unknown Error")
    except sr.WaitTimeoutError:
        print("WaitTimeout Error")
    except UnboundLocalError:
        print("Not saved")
    #sleep(1)

freeze_support()