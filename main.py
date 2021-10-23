import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyttsx3




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jack' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play ' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who is ' in command:
        person = command.replace('who is' ,  '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date =datetime.datetime.now().strptime('%D:%M:%Y')
        talk('Current date is')
    elif 'are you single' in command:
        talk('No I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am fine, how are you')
    elif 'listen your voice' in command:
        talk('thankyou, how can i help you ')
    elif 'help' in command:
        talk('yes sure, you just command me what you want')
    elif 'love' in command:
        talk('i love you too')
    elif 'what is your name' in command:
        talk('my name is jack')
    elif 'age' in command:
        talk('I am elder enough to get covid vaccine dose')
    elif 'search' in command:
        say = command.replace('search', '')
        talk('searching' + say)
        info = webbrowser.open('http://google.com/search?q='+command)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()