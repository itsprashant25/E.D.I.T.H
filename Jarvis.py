import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING!")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am EDITH sir Please tell me how can i help you ")
    
def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("itsprashantofficial25@gmail.com","Shivam#111")
    server.sendmail("itsprashantofficial25@gmail.com", to,content)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wikipedia')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak("Opening youtube!")
            webbrowser.open('youtube.com')
        elif 'gfg' in query:
            speak( "opening geeks for geeks")
            webbrowser.open( 'geeksforgeeks.com')
        elif 'google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'time' in query:
            t=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir The time is {t}')
        elif 'open code' in query:
            codepath="C:\\Users\HP\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile( codepath)
        elif 'send email' in query:
            try:
               speak("sir what should i say")
               content=takecommand()
               to="prashantkumar262757@gmail.com"
               sendmail(to,content)
               speak("Sir your mail has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry prashant sir your mail cant be send")
                
            