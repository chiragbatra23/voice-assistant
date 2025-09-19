import speech_recognition as sr
import os
import webbrowser
import datetime


def say(text):
    os.system(f'say "{text}"')  # MacOS built-in TTS


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... please wait")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening now...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")  # use "en-IN" or "hi-IN"
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Error:", e)
        return ""


if __name__ == "__main__":
    print("Pycharm")
    say("Hello chirag, i am your personal A.I  How can I help?")

    while True:
        print("Listening...")
        query = takecommand()

        if query == "":
            continue

        # --- Websites ---
        sites = [
            ("youtube", "https://www.youtube.com"),
            ("wikipedia", "https://www.wikipedia.com"),
            ("google", "https://www.google.com")
        ]

        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]}, sir")
                webbrowser.open(site[1])

        # --- Time ---
        if "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        # --- Apps ---
        if "open facetime" in query.lower():
            os.system("open /System/Applications/FaceTime.app")
            say("Opening FaceTime")

        if "open whatsapp" in query.lower():
            os.system("open /Applications/WhatsApp.app")
            say("Opening WhatsApp")

        if "open camera" in query.lower():
            os.system("open /System/Applications/Image Capture.app")
            say("opening camera")

