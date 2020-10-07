import speech_recognition as sr
for i,n in enumerate(sr.Microphone.list_microphone_names()):
    print(i,n)