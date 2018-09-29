import pyaudio
import speech_recognition as sr
import os
import webbrowser
import pyautogui as p
import time

#start of the first speech input
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say anything")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
    except:
        print("Sorry could not recognize that.")
    
    if "Chrome" or "Google" in text:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    elif "search" in text:
        
        #start of the second speech input
        r_1 = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("What would you like to search for?")
            audio_1 = r_1.listen(source)
            
            try:
                text_1 = r_1.recognize_google(audio_1)
                print("you said : {}".format(text_1))
            except:
                print("Sorry could not recognize that.")
            
        webbrowser.open("https://www.google.com/search?q=" + text_1)
        time.sleep(4) #delay for browser to open
        if "youtube" or "video" in text_1:
            p.click(588,553)





#Lets you get mouse position
import win32api
x, y = win32api.GetCursorPos()
print(x,y)
