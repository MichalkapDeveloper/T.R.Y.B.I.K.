import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='pl-PL')
        print("User said: %s" % query)

    except Exception as e:
        print(e)
        print("Google was unable to hear")
        return "ERROR"

    return query.lower()
