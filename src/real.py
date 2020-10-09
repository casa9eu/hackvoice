import nvg
import json
import pyttsx3 as px
import speech_recognition as sr
from datetime import datetime as dt
from multiprocessing import Process
from time import sleep

r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = px.init()

def speak():
    try:
        with open("queue.json", "r") as f:
            queue = json.loads(f.read())
    except OSError:
        queue = False

    if (queue):
        for q in queue:
            nvg.FileSaver.Save(q)
            print(q)
            voice.say(q)
            voice.runAndWait()
            voice.stop()
        with open("queue.json", "w") as f:
            f.write(json.dumps([]))

def GetVoice():
    try:
        with open("queue.json", "r") as f:
            queue = json.loads(f.read())
    except OSError:
        queue = []
    try:
        with m as source:
            print(f"[{dt.now().date()}, {str(dt.now().time())[:-7]}]:",end=" ")
            audio = r.listen(source, timeout=2, phrase_time_limit=3)
        text = r.recognize_google(audio, language="ru-RU").lower()
        queue.append(text)
        with open("queue.json", "w") as f:
            f.write(json.dumps(queue))

    except sr.UnknownValueError:
        print("Unknown Error")
    except sr.WaitTimeoutError:
        print("WaitTimeout Error")
    except UnboundLocalError:
        print("Not saved")

if __name__ == "__main__":
    with m as source:
        r.adjust_for_ambient_noise(source)

    while True:
        p1 = Process(target=GetVoice)
        p1.start()
        p2 = Process(target=speak)
        p2.start()
        p1.join()
        p2.join()
        sleep(0.1)