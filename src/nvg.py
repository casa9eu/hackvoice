class FileSaver:
    def Save(new_text, path = "dialog.txt"):
        try:
            with open(path, "r") as f:
                text = f.read()
        except OSError:
            pass
        with open(path, "w") as f:
            f.write(text + "\n" + str(new_text))

class Speaker:
    def __init__(self, speaker = 0):
        pass



# def GetVoiceCallback(r, audio):
#     my_words = r.recognize_google(audio, language="ru-RU").lower()
#     print(my_words)
#     speak(my_words)