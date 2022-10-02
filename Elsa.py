import ctypes
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import winshell as winshell
import wolframalpha
import requests
from playsound import playsound
import os
from gtts import gTTS
from googletrans import *
import subprocess

languages = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
             'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
             'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn',
             'bosnian', 'bs', 'bulgarian', 'bg', 'catalan', 'ca',
             'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
             'zh-cn', 'chinese (traditional)', 'zh-tw', 'corsican', 'co',
             'croatian', 'hr', 'czech', 'cs', 'danish', 'da', 'dutch', 'nl',
             'english', 'en', 'esperanto', 'eo', 'estonian', 'et',
             'filipino', 'tl', 'finnish', 'fi', 'french', 'fr',
             'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka',
             'german', 'de', 'greek', 'el', 'gujarati', 'gu',
             'haitian creole', 'ht', 'hausa', 'ha', 'hawaiian', 'haw',
             'hebrew', 'he', 'hindi', 'hi', 'hmong', 'hmn',
             'hungarian', 'hu', 'icelandic', 'is', 'igbo', 'ig',
             'indonesian', 'id', 'irish', 'ga', 'italian', 'it',
             'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
             'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko',
             'kurdish (kurmanji)', 'ku', 'kyrgyz', 'ky', 'lao', 'lo',
             'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt',
             'luxembourgish', 'lb', 'macedonian', 'mk', 'malagasy', 'mg',
             'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori', 'mi',
             'marathi', 'mr', 'mongolian', 'mn', 'myanmar (burmese)', 'my',
             'nepali', 'ne', 'norwegian', 'no', 'odia', 'or', 'pashto', 'ps',
             'persian', 'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
             'romanian', 'ro', 'russian', 'ru', 'samoan', 'sm',
             'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 'st',
             'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si', 'slovak', 'sk',
             'slovenian', 'sl', 'somali', 'so', 'spanish', 'es', 'sundanese', 'su',
             'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil', 'ta',
             'telugu', 'te', 'thai', 'th', 'turkish', 'tr', 'ukrainian', 'uk',
             'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 'uz', 'vietnamese', 'vi',
             'welsh', 'cy', 'xhosa', 'xh', 'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishes():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")
    time.sleep(1)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        speak("I'm Listening")
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            statement = r.recognize_google(audio, language='en')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, please say that again...")
            return "None"
        return statement


def destination_language():
    to_lang = takeCommand()
    while to_lang == "None":
        to_lang = takeCommand()
    to_lang = to_lang.lower()
    return to_lang


print('Loading your AI personal assistant Elsa')
speak("Loading your AI personal assistant Elsa")
wishes()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Elsa is shutting down, Good bye')
            print('your personal assistant Elsa is shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world")
            speak('Here are the world news from BBC News, Happy reading')
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions, what question do you want to ask now?')
            question = takeCommand()
            app_id = "7L847Y-PKK5KTHV3R"
            client = wolframalpha.Client('7L847Y-PKK5KTHV3R')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "translate" in statement:
            print("What do you want to translate?")
            speak("What do you want to translate?")
            statement = takeCommand()
            print("What is the translation language?")
            speak("What is the translation language?")
            to_lang = destination_language()
            while to_lang not in languages:
                speak("Sorry, this language isn't available, try another one please...")
                print("Sorry, this language isn't available, try another one please...")
                to_lang = destination_language()
            to_lang = languages[languages.index(to_lang) + 1]
            translator = Translator()
            text_to_translate = translator.translate(statement, dest=to_lang)
            text = text_to_translate.text
            speaks = gTTS(text=text, lang=to_lang, slow=False)
            audio_file = os.path.dirname(__file__) + 'captured_voice.mp3'
            speaks.save(audio_file)
            playsound(audio_file)
            os.remove(audio_file)
            print(text)
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Elsa version 1 point 0 your personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow, predict time, search wikipedia,'
                  ' predict weather in different cities,find any location, writing notes, get the world news'
                  ' from BBC News and you can ask me computational and geographical questions too!')
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "weather" in statement:
            api_key = "435a1bcf6e9597b330cfec0428f6bc57"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Mr. Wahab Tlays")
            print("I was built by Mr. Wahab Tlays")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "thank you" in statement or "thanks" in statement:
            speak("My pleasure Sir")
            print("My pleasure Sir")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "how are you" in statement:
            speak("I'm well, thank you")
            speak("How are you, Sir?")
            resp = takeCommand()
            if 'fine' in resp or "good" in resp:
                speak("It's good to know that you're fine")
            elif 'not good' in resp or 'bad' in resp or 'not fine' in resp:
                speak("I'm sorry to hear that")
            else:
                speak("I don't understand that, but I wish you're fine")

        elif 'lock window' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            break

        elif 'shutdown system' in statement:
            speak("Hold On a Sec ! Your system is on its way to shut down, make sure there is no unsaved data")
            subprocess.call('shutdown / p /f')
            break

        elif 'empty recycle bin' in statement:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "don't listen" in statement or "stop listening" in statement:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "location" in statement:
            print("What's the city name?")
            speak("What's the city name?")
            c_name = takeCommand()
            location = str(c_name)
            speak("User asked to Locate" + location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "write a note" in statement:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Elsa.txt', 'w')
            speak("Sir, Should i include date and time")
            respond = takeCommand()
            if 'yes' in respond or 'sure' in respond:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                print("It's done sir")
            else:
                file.write(note)
                print("It's done sir")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "show note" in statement:
            speak("Showing Notes")
            file = open("Elsa.txt", "r")
            print(file.read())
            speak(file.read())
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "will you be my girl friend" in statement or "will you be my boy friend" in statement:
            speak("I'm not sure about, may be you should give me some time")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break

        elif "i love you" in statement:
            speak("It's hard to understand")
            speak("Anything else, Sir?")
            ate = takeCommand()
            if "yes" in ate or "sure" in ate:
                continue
            else:
                speak("Okay Sir")
                break
time.sleep(3)
