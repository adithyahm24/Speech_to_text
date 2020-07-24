import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    text = input("Enter the text to speech : ")
    eng = pyttsx3.init()
    eng.say(text)
    eng.runAndWait()


def speech_to_text():
    global q
    r = sr.Recognizer()
    r.dynamic_energy_threshold =False
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=6)

    try:
        print('Recognising...')
        q = r.recognize_google(audio,language='en-in')
        print(q)
        return q
    except Exception as e:
        print(e)


speech_to_text()