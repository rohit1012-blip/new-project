import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import webbrowser
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# Text-to-speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Convert speech to text
def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Sorry, I couldn't hear that. Please say that again.")
        return "none"
    return query

# Function to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)

    tt = datetime.datetime.now().strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}") 

    speak("I am Jarvis, sir. How can I assist you today?")
    
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('rohitsinghcontactus@gmail.com', 'nbum dtgl pfyl vewi')
#     server.sendmail('rohitsinghcontactus@gmail.com',to,content)
#     server.close()
    
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=14611042a83b4cca8073a57422e5cab4'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")
    
def time():
        time = int(datetime.datetime.now().time)
    

if __name__ == "__main__":
    wish()

    while True:
   
        query = takecomand().lower()

        # Logic for tasks
        if "open notepad" in query:
            try:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)
                speak("Opening Notepad.")
            except Exception as e:
                speak("Sorry, I couldn't open Notepad.")
                print(f"Error: {e}")
                
        elif "open powerpoint" in query:
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(npath)
            speak("Opening Powerpoint")
            
        elif"open command prompt" in query:
            os.system("start cmd")
            
        elif"open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(58)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
      
        elif"ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        
        
        elif"wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)
       
            
                
        elif"open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif"open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif"open google" in query:
            speak("sir, what should i search on google")
            cm = takecomand().lower()
            webbrowser.open(f"{cm}")
            #open google and search with command
            
        elif"send message" in query:
            
            phone_numbers = ["+918777043134", "+919163862769", "+916299025927"]
            message = "This is a testing message"
            for number in phone_numbers:
                kit.sendwhatmsg(number, message, 0, 2)

           #send message on whatsapp  using pywhatkit library
           
        elif"play music " in query:
            speak("sir, which song should i search in youtube")
            kit.playonyt(takecomand().lower())
        
        # elif"send email " in query:
        #     try:
        #         speak("what should i say ?")
        #         content = takecomand().lower()
        #         to = "paramanikshubhankar302@gmail.com"
        #         sendEmail(to,content)
        #         speak("email has been sent to sanku")
                
        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir, i am not able to sent this mail to sanku")   
                
        elif"thanks" in query:
            speak("thanks for using me sir, have a great day.")
            sys.exit()
            
        elif"close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill/f/im notepad.exe")
            
        elif"tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif"shutdown the system" in query:
            os.system("shutdown /s /t 5")
            
        elif"switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
        elif"tell me news" in query:
            speak("please wait sir , fetaching the latest news") 
            news() 
                    
        elif"email to friend" in query:
            
            speak("sir what should i say")
            query = takecomand().lower() 
            if"send a file" in query:
                email = 'rohitsinghcontactus@gmail.com' 
                password = 'nbum dtgl pfyl vewi'
                send_to_email = 'paramanikshubhankar302@gmail.com'
                speak("okay sir, what is the subject for this email")
                query = takecomand().lower()
                subject = query
                speak("and sir, what is the message for this email")
                query2 = takecomand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")
                
                speak("please wait,i am sending email now")
                
                msg = MIMEMultipart()
                msg['from'] = email
                msg['to'] = send_to_email
                msg['subject'] = subject
                
                msg.attach(MIMEText(message, 'plain'))
                
                filename = os.path.basename(file_location)
                attachment = open(file_location,"rb")
                part = MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('content-disposition',"attachment; filename = %s" %filename)
                
                msg.attach(part)
                
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email,text)
                server.quit()
                speak("email has been sent to friend")
                
            else:
                email = 'rohitsinghcontactus@gmail.com'
                password = 'nbum dtgl pfyl vewi'
                send_to_email = 'paramanikshubhankar302@gmail.com'
                message = query
                
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email, password)
                
                server.sendmail(email, send_to_email,message)
                server.quit()
                speak("email has been sent to friend")
                
                
        speak("sir, do you have any other work")