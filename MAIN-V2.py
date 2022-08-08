import datetime
import random
import smtplib
import sys
import webbrowser
import textwrap

import pyttsx3
import wikipedia
import os
import time
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("AMUNET")
root.geometry('755x620')
print("Amunet ACTIVE....")
MASTER = "Valetrix"
songly = -1

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.in",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except:
        open_url(f"https://www.google.com/search?q={search_query}")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("Amunet is Online. How may I help you today?")


speak("Initializing Amunet....")
wishMe()
def query(q):
    query = q

    # logic for executing basic tasks

    if "what's up" in query or "how are you" in query:
        stMsgs = [
            "Just doing my thing!",
            "I am fine!",
            "Nice!",
            "I am nice and full of energy",
        ]
        z2.config(text=random.choice(stMsgs))
        speak(random.choice(stMsgs))

    elif "wikipedia" in query.lower():
        query_n = query.replace("wikipedia", "")
        z2.config(text=f"Searching wikipedia for {query_n}....")
        speak(f"Searching wikipedia for {query_n}....")
        try:
            x = ''
            results = wikipedia.summary(query_n, sentences=2)
            my_wrap = textwrap.TextWrapper(width = 40)
            wrap_list = my_wrap.wrap(text=results)
            for line in wrap_list:
                x = x + f'{line}\n'
            z2.config(text=x)
            speak(results)
        except Exception as e:
            z2.config(text=query_n + '- page on wikipedia does not exist')
            speak(f'Sorry Sir but a {query_n} page does not exist or cannot be '
                  f'found on wikipedia, do you want me to search google??')
            gq = z.get()
            if 'yes' in gq.lower() or 'ya' in gq.lower() or 'sure' in gq.lower() \
                                                    or 'of course' in gq.lower():
                z2.config(text='Searching Google....Please Wait for a few minutes')
                search(query_n, 'google')
                speak('Searching Google....Please Wait for a few minutes!!!!')
            elif 'no' in gq.lower() or 'nope' in gq.lower() or 'na' in gq.lower() \
                                                    or 'what ever' in gq.lower():
                z2.config(text="Okay Sir, I won't search Google")
                speak("Okay Sir, I won't search Google")
            else:
                z2.config(text="Sorry, I didn't get that..")
                speak('''Sorry, i didn't get that''')
    elif "open" in query.lower():
        website = query.replace("open", "").strip().lower()
        try:
            open_url(popular_websites[website])
        except IndexError:  # If the website is unknown
            z2.config(text=f"Unknown website: {website}")
            speak(f"Sorry, i don't know the website {website}")

    elif "search" in query.lower():
        search_query = query.split("for")[-1]
        search_query = search_query.replace('search', '')
        z2.config(text=f'Searching For {search_query}')
        speak(f'Searching For {search_query}')
        search(search_query, 'google')
    elif "nothing" in query.lower() or "stop" in query.lower():
        z2.config(text='Okay, Bye Sir, have a good day!')
        speak("okay")
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "hello" in query.lower() or 'hi' in query.lower():
        z2.config(text='Hello Sir!')
        speak("Hello Sir")

    elif "bye" in query.lower():
        z2.config(text="Bye Sir, have a good day.")
        speak("Bye Sir, have a good day.")
        sys.exit()
    elif 'say' in query.lower():
        query = query.replace('say', '')
        z2.config(text=query)
        speak(query)
    elif "abort" in query.lower():
        say = ['Copy That!!', 'Roger!!']
        ran = random.randint(0, 1)
        z2.config(text=f'{say[ran]}, Sytems Aborted!!Repeat!!Amunet Systems Aborted!!!')
        speak(say[ran])
        speak("Sytems Aborted!!Repeat!!Amunet Systems Aborted!!!")
        sys.exit()
    elif 'time' in query.lower():
        time_c = int(time.strftime('%H'))
        time_h = int(time.strftime('%I'))
        time_m = int(time.strftime('%M'))
        if time_c >= 12 and time_c < 24:
            z2.config(text=f'TIME = {time_h}:{time_m}PM')
            speak(f'The time now is {time_h} {time_m}...')
        elif time_c <= 0 and time_c < 12:
            print(f'TIME = {time_h}:{time_m}AM')
            speak(f'The time now is {time_h} {time_m} AM...')
    elif 'date' in query.lower():
        time_d = int(time.strftime('%d'))
        time_M = int(time.strftime('%m'))
        time_M_n = time.strftime('%b')
        time_y = int(time.strftime('%Y'))
        z2.config(text=f'Date = {time_d}/{time_M}/{time_y}')
        speak(f'The date today is, {time_d}th of {time_M_n} {time_y}...')
    elif "play" in query.lower():
        query = query.replace('play', '')
        z2.config(text=f"Playing {query}")
        speak(f"Playing {query}")
        open_url(f"https://www.youtube.com/results?search_query={query}")
    elif "commands_help" in query.lower() or 'help' in query.lower():
        z2.config(text="Commands = Date, Time, Music, Play, Say, Search, Hello, Bye, Abort, Nothing, Open, Wikipedia, What's Up.")
        speak("""Commands are Date, Time, Music, Play, Say, Search, Hello, Bye, Abort, Nothing, Open, Wikipedia, What's Up.""")
    else:
        speak("""Sorry sir, i am unable to do that currently""")
        z2.config(text="Sorry sir, i am unable to do that currently")

    speak("What else can i help  you with sir?")


lf = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf2 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf.pack(pady=10)
lf2.pack(pady=10)
z2 = customtkinter.CTkLabel(lf2, text="AMUNET ACTIVE", text_font=('Agency FB', 19))
z = customtkinter.CTkEntry(lf, width=300, height=30, text_font=('Agency FB', 19), corner_radius=20)
z3 = customtkinter.CTkButton(lf, text='ASK', command=lambda: query(z.get()), height=30, corner_radius=20)
z.grid(row=0,column=0, padx=10, pady=10)
z2.grid(row=0,column=0, padx=10, pady=10)
z3.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
