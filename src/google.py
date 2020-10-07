from gtts import gTTS
from io import BytesIO

def speak_g(text, file=False):
    mp3_fp = BytesIO()
    language = 'ru'
    speech = gTTS(text=text, lang=language, slow=False)
    if(file):
        speech.save("t.mp3")
    else:
        speech.write_to_fp(mp3_fp)

#import os
#os.system("start t.mp3")