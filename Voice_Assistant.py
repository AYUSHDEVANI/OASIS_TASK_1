import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()


engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening.........")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said: ",text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error: {e}")
            return ""

