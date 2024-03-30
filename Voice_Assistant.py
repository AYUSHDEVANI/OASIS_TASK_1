import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia

recognizer = sr.Recognizer()


engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening.........")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio,  language="en-in")
            print("You said: ",text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error: {e}")
            return ""

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()


def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today`s date is {current_date}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        command = command.replac("wikipedia","")
        results = wikipedia.summary(command,sentences = 5)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open notepad" in command:
        speak("Opening Notepad please wait a moment.")    
        path = "C:/Windows/System32/notepad.exe"
        os.startfile(path)
    
    elif "close notepad" in command:
        speak("Closing notepad please wait.........")
        os.system("C:/Windows/System32/taskkill.exe /F /IM notepad.exe")
    
    elif "open youtube" in command:
        speak("Here you go to youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in command:
        speak("Please wait Google is ready for you....")
        webbrowser.open("https://www.google.co.in/")
    
    elif "open mail" in commans:
        speak("Here you go to mail ......")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif "open whatsapp" in command:
        speak("Open Whatsapp please wait a moment............")
        webbrowser.open("https://web.whatsapp.com/")
    


    elif "search" in command:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
        else:
            speak("Sorry, I didn`t catch that. Please try again.")
    else:
        speak("Sorry, I didn`t understand that command.")

def greet():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour<12:
        speak("Good Morning !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
    else:
        speak("Good Night!!")
    speak("Welcome, I am Your personal Google Assistant.")

def main():
    # speak("Hello, How can I assist you today?")
    greet()

    while True:
        command = listen()
        if "goodbye" in command:
            speak("Goodbye, Have a great Day!")
            break
        handle_command(command)

if __name__ == "__main__":
 
    main()