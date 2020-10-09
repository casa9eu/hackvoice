import nvg
import pyttsx3 as px
import speech_recognition as sr
from datetime import datetime as dt

r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = px.init()
queue = []

def speak(text):
    voice.say(text)
    voice.runAndWait()
    voice.stop()

def GetVoice(a=0):
    with m as source:
        print(f"[{dt.now().date()}, {str(dt.now().time())[:-7]}]:",end=" ")
        audio = r.listen(source, timeout=20, phrase_time_limit=30)
    queue.append(r.recognize_google(audio, language="ru-RU").lower())

if __name__ == "__main__":
    with m as source:
        r.adjust_for_ambient_noise(source)

    voices = voice.getProperty('voices')
    voice.setProperty('voice', voices[-1].id)

    while True:
        try:
            GetVoice()

            if (queue):
                my_words = queue[-1]
                nvg.FileSaver.Save(my_words)
                print(my_words)
                speak(my_words)

        except sr.UnknownValueError:
            print("Unknown Error")
        except sr.WaitTimeoutError:
            print("WaitTimeout Error")
        except UnboundLocalError:
            print("Not saved")