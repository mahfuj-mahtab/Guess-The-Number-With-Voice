import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(any_str):
    engine.say(any_str)
    engine.runAndWait()


def take_command():
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        audio= r.listen(source)
        
    try:
        query = r.recognize_google(audio)
        return query
        
    except:
        speak("Sorry say that again")


def wish_me():
    speak("Good morning")


def guess():
    speak("Hey I want to play guess the number game please choose a number")
    time.sleep(5)
    speak("did you choose the number?")
    speak("now can you please multiply the chosen number by 2?")
    time.sleep(5)
    speak("now can you please add 10?")
    time.sleep(3)
    speak("now can you please divide the number by 2")
    time.sleep(3)
    speak("subtract your original number from the equation")
    time.sleep(3)
    speak("Now you have have 5 right?")
# while(1==1):
#     take_command()

if __name__=="__main__":
    wish_me()
    guess()
