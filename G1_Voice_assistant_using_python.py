
import speech_recognition as sr
import pyttsx3


# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Sorry, speech recognition service is down.")
            return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    command = listen().lower()

    if "hello" in command:
        speak("Hello there!")

    elif "goodbye" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't catch that.")

