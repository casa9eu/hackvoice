import time
import speech_recognition as sr

def callback(recognizer, audio):
    try:
        print(recognizer.recognize_google(audio, language="ru-RU"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone(device_index=1)
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)