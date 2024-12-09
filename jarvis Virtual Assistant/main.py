import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI 
from gtts import gTTS
import pygame
import os

#pip install pocketSphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="d093053d72bc40248998159804e0e67d"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the Mp3 File
    pygame.mixer.music.load('temp.mp3')

    # Play the Mp3 file
    pygame.mixer.music.play()

    # keep the program running until the music stop playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    os.remove("temp.mp3")  

def aiProcess(command):
    client = OpenAI(
        api_key ="sk-proj-WxS17ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bqZaFTcj",
    )

    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        message=[
            {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like     and goofle cloud .Give short responses please"},
            {"role":"user","content":command}
        ]
    )
    return (completion.choices[0].message.content)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open Youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link =  musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #Paras the JSON response
            data = r.json()

        #Extract the articles
        articles =data.get('articles',[])

        #speak the headlines
        for article in articles:
            speak(article['title'])

    else:
        #Let open Ai handel the request
        output = aiProcess(c)
        speak(output)
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis ...")
    while True:
        #Listen For the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing....")
        
        # reconize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening ....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak ("Yes")
                #Listen For A  Command
                with sr.Microphone() as source:
                    print("Jarvis Active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    

        except  Exception as e:
            print("Error ;{0}".format(e))
