# importing modules and pakages

import pyttsx3
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import time

# voice modulating

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# starting of main function and logics

def main():

# speak function

    def speak(audio):
    	engine.say(audio)
    	engine.runAndWait()

# wishMe function

    def wishMe():
    	hour = int(datetime.datetime.now().hour)
    	if hour>=0 and hour<12:
    		speak("Good Morning Mintplay")
    	else:
    		speak("Welcome back Matrix")

# takeCommand function

    def takeCommand():
    	r = sr.Recognizer()
    	with sr.Microphone() as source:
    		print("Listening....")
    		audio = r.listen(source)
    	try:
    		print("Recognizing")
    		query = r.recognize_google(audio, language='en-in')
    		print(f"Did you mean: {query}\n")
    		speak(f"You said: {query}\n")
    	except Exception as e:
    		print("Sorry I could not hear you")
    		speak("Sorry Would you mind repeating that phrase again")
    		query = None
    	return query

    speak("Initializing Pluto")
    print("Initializing Pluto")

    wishMe()
    query = takeCommand()
# logic starts
    if "Wikipedia" in query:
    	speak("Searching the Wikipedia...")
    	print("Searching the Wikipedia....")
    	query = query.replace("Wikipedia", "")
    	results = wikipedia.summary(query, sentences=5)
    	print(results)
    	speak("According to the Wikipedia" + " " + results)

    elif 'music' in query:
        speak("Allright Openning Spotify")
        print("Allright Openning Spotify")
        os.startfile('Spotify.exe')

    elif 'open YouTube' in query:
        speak("Openning YouTube")
        print("Here You go")

        webbrowser.open("www.youtube.com")
    elif 'open Google' in query:
        speak("Openning Google")
        print("Openning Google")
        webbrowser.open("www.google.com")

    elif 'browser' in query:
        speak("Openning Chrome")
        print("Openning Chrome")
        os.startfile('chrome.exe')

    elif 'who created you' in query:
        speak("I am made by Matrix using python")
        print("Matrix made me using python")

    elif 'who is matrix' in query:
        speak("He is a teen living in India")
        print("He is a teen living in India")

    elif 'search' in query:
        speak("Searching the internet")
        print("Searching")
        logic = query.replace("search", "")
        webbrowser.open(logic)

    elif 'date' in query:
        bot_date = datetime.datetime.now().today()
        print(bot_date)
        speak(bot_date)

    elif 'time' in query:
        bot_time = datetime.datetime.now()
        print(bot_time.strftime("%I:%M"))
        speak(bot_time.strftime("%I:%M"))

    elif 'pictures' in query:
        speak("Searching in pictures")
        print("Searching")
        pic_logic = query.replace("pictures", "")
        webbrowser.open(pic_logic)

    elif 'exit' in query:
        speak("Alright exiting, .... thanks for your time")
        exit()

    elif 'who are you' in query:
        print("I am an virtual assistant. My name is Pluto and I am made by Matrix.  I am truly grateful to him. Thanks Matrix if you are hearing this")
        speak("I am an virtual assistant. My name is Pluto and I am made by Matrix.  I am truly grateful to him. Thanks Matrix if you are hearing this")

    elif 'when were you born' in query:
        print("I was born on 10th August, 2020,   I still rember that beautiful moment")
        speak("I was born on 10th August, 2020,   I still rember that beautiful moment")

# end of logic

main()