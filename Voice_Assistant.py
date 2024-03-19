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