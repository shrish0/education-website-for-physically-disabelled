from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3
# import subprocess
# import wolframalpha
# import random
# import wikipedia
# import webbrowser
# import os
# import winshell
# import pyjokes
# import feedparser
# import smtplib
# import datetime 
# import json
# import requests
# # from twilio.rest import Client
# from bs4 import BeautifulSoup
# import win32com.client as wincl
# from urllib.request import urlopen
from PIL import Image 
# import shutil


driver = webdriver.Chrome('C:\\xampp\\htdocs\\botedu\\voice-assistant-main')
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
time.sleep(1)
speak("Hello master! I am now online..")
sh="12"
while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' in voice:
        speak('Opening google..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(window_list[-1])
        driver.get('https://google.com')
    elif 'search google' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element("id","APjFqb")
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'news' in voice:
         try:
            response = requests.get('https://www.bbc.com/news')
            b4soup = BeautifulSoup(response.text, 'html.parser')
            headLines = b4soup.find('body').find_all('h3')
            unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                        'News daily newsletter', 'Mobile app', 'Get in touch']
            i=0
            for x in list(dict.fromkeys(headLines)):
                i+=1
                if x.text.strip() not in unwantedLines:
                        print(x.text.strip())
                        speak(x.text.strip())
                if i==5:
                    break
         except Exception as e: 
                print(str(e))

    elif 'message' in voice:
        try:
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element("name","message")
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Not a valid command. Please try again.')

    elif 'subject' in voice:
        try:
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element("name","subject")
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Not a valid command. Please try again.')


    elif 'mail' in voice:
        try:
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element("name","email")
            element.clear()
            element.send_keys(query+"@gmail")
            element.send_keys(Keys.RETURN)
        except:
            speak('Not a valid command. Please try again.')


    # elif "write note" in voice :
    #     pass

    # elif "blind" in voice :
    #     try:
    #         print(driver.find_element(By.xpath("/html/body")).text)

    #         speak('Goodbye Master!')
    #     except:
    #         speak('Goodbye Master!')
    #     pass
    # elif 'joke' in voice:
    #     speak(pyjokes.get_joke())

    elif "take screenshot" in voice :
        try:
            speak("save as ?")
            query = recognize_speech()
            get_url = driver.current_url
            driver.get(get_url)
            time.sleep(2)
            screenshot = driver.save_screenshot("botedu\\voice-assistant-main\screenshot\\"+query+".png")
            
        except:
            speak('not a valid command')
    
    elif 'name' in voice:
        try: 
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element("name","name")
            element.clear()
            element.send_keys(query)  
            element.send_keys(Keys.RETURN)
        except:
            speak('Not a valid command. Please try again.')

    elif "down" in voice:
        try:
            driver.execute_script("window.scrollBy(0,400)")
        except:
            speak('Not a valid command. Please try again.')
            
    elif "upward" in voice: 
        try:
            driver.execute_script("window.scrollBy(0,-400)")
        except: 
            speak('Not a valid command. Please try again.')

            
    elif "top" in voice:
        try:
            driver.execute_script("window.scrollBy(0,-5000)")
        except:
            speak('Not a valid command. Please try again.')

            
    elif "bottom" in voice:
        try:
            driver.execute_script("window.scrollBy(0,5000)")
        except:
                 speak('Not a valid command. Please try again.')

            
    elif 'open youtube' in voice:
        try:
            speak('Opening youtube..')
            driver.execute_script("window.open('');")
            window_list = driver.window_handles
            driver.switch_to.window(window_list[-1])
            driver.get('https://youtube.com')
        except:
            speak("not a valid command")
    elif 'open website' in voice:
        try:
            speak('Opening edubot..')
            driver.execute_script("window.open('');")
            window_list = driver.window_handles
            driver.switch_to.window(window_list[-1])
            driver.get('http://localhost/botedu')
        except:
            speak("not a valid command")
    elif "open screenshot" in voice:
        try:
            driver.get('http://localhost/botedu/voice-assistant-main/screenshot')
            speak("name opening image?")
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            driver.get('http://localhost/botedu/voice-assistant-main/screenshot//'+query+".png")

        except:
            pass
    # elif voice in "home about courses contact":
    #     element=driver.find_element("id" ,voice).click()
    #     speak("locating to "+voice)
    elif "home" in voice:
        try:
            element=driver.find_element("id" ,"home").click()
            speak("locating to "+voice)
        except:
            speak("not a valid command")
        # element.send_keys(Keys.RETURN)
    elif "about"  in voice:
        try:
            element=driver.find_element("id" ,"about").click()
            speak("locating to "+voice)
        except:
            speak("not a valid command")
        # element.send_keys(Keys.RETURN)
    elif "contact" in voice:
        try:
            element=driver.find_element("id" ,"contact").click()
            speak("locating to "+voice)
        except:
            speak("not a valid command")
        # element.send_keys(Keys.RETURN)
    elif "courses"  in voice:
        try:
            element=driver.find_element("id" ,"courses").click()
            speak("locating to "+voice)
        except:
            speak("not a valid command")
        # element.send_keys(Keys.RETURN)
    elif "submit" in voice:
        try:
            element=driver.find_element("id" ,"send").click()
            # speak("locating to "+voice)
            # element.send_keys(Keys.RETURN)
        except:
            speak("not a valid command")

    elif 'search youtube' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'switch tab' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to.window(driver.window_handles[cur_tab])
    elif 'close tab' in voice:
        speak('Closing Tab..')
        driver.close()
    elif 'go back' in voice:
        try:
             driver.back()
        except:
            speak("not a valid command")
        
    elif 'go forward' in voice:
        try:
           driver.forward()
        except:
            speak("not a valid command")
    elif 'biology' in voice:
        try:
            element = driver.find_element('id','biology'+sh).click()
        except:
            speak("not a valid command")
    elif 'physics' in voice:
        try:
            element = driver.find_element('id','physics'+sh).click()
        except:
            speak("not a valid command")
    elif 'chemistry' in voice:
        try:
            element = driver.find_element('id','chemistry'+sh).click()
        except:
            speak("not a valid command")
    elif 'mathematics' in voice:
        try:
            element = driver.find_element('id','math'+sh).click()
        except:
            speak("not a valid command")
    elif 'science' in voice:
        try:
            element = driver.find_element('id','science'+sh).click()
        except:
            speak("not a valid command")
    elif 'sst' in voice:
        try:
            element = driver.find_element('id','sst'+sh).click()
        except:
            speak("not a valid command")
    elif 'hindi' in voice:
        try:
            element = driver.find_element('id','hindi'+sh).click()
        except:
            speak("not a valid command")
    elif 'english' in voice:
        try:
            print("english"+sh)
            element = driver.find_element('id','english'+sh).click()
        except:
            speak("not a valid command")
    elif 'class 9' in voice:
        try:
            element = driver.find_element('name','Class 9').click()
            sh="9"
        except:
            speak("not a valid command")
    elif 'class 8' in voice:
        try:
            element = driver.find_element('name','Class 8').click()
            sh="8"
        except:
            speak("not a valid command")
    # elif 'class 5' in voice:
    #         element = driver.find_element_by_xpath("// a[contains(text(),\'class ')]").click()   
    elif 'class 10' in voice:
        try:
            element = driver.find_element('name','Class 10').click()
            sh="10"
        except:
            speak("not a valid command")
    
        
    elif 'class 12' in voice:
        try:
            element = driver.find_element('id','defaultOpen').click()
            sh="12"
        except:
            speak("not a valid command")
    
        
    elif 'class 7' in voice:
        try:
            element = driver.find_element('name','Class 7').click()
            sh="7"
        except:
            speak("not a valid command")

    elif 'class 6' in voice:
        try:
            element = driver.find_element('name','Class 6').click()
            sh="6"
        except:
            speak("not a valid command")
    elif 'class 5' in voice:
        try:
            element = driver.find_element('name','Class 5').click()
            sh="5"
        except:
            speak("not a valid command")
    elif 'class 4' in voice:
        try:
            element = driver.find_element('name','Class 4').click()
            sh="4"
        except:
               speak("not a valid command")

    # elif 'class 3' in voice:
    #     element = driver.find_element('name','Class 3').click()
    # elif 'class 2' in voice:
    #     element = driver.find_element('name','Class 2').click()
    
    elif 'class 11' in voice:
        try:
            element = driver.find_element('name','Class 11').click()
            sh="11"
        except:
             speak("not a valid command")

    
    elif "open note" in voice:
        #testing
        try:

            speak('Opening notes..')
            driver.execute_script("window.open('');")
            window_list = driver.window_handles
            driver.switch_to.window(window_list[-1])
            # driver.switch_to.window(window_list[-1])
            driver.get('http://localhost/botedu/voice-assistant-main/notes.txt')
        except:
            speak("not a valid command")
        

    elif "write a note" in voice:
        try:

            while True:
                speak('I am listening..')
                query = recognize_speech()
                
                if query == 'Error':
                    continue
                elif query == 'break':
                    break
                file1 = open("botedu\\voice-assistant-main\\notes.txt", "a")  # append mode
                file1.write("\n"+query)
                print(query)   
                file1.close()
            speak("done")
        except:
            speak('Not a valid command. Please try again.')
        
        pass
    elif "play" in voice:
        try:
            element = driver.find_element("id","c1").click()
        except:
            speak('Not a valid command. Please try again.')
    elif "stop" in voice:
        try:
            element = driver.find_element("id","c1").click()
        except:
            speak('Not a valid command. Please try again.')
        # driver.switch_to.frame(iframe)

        # element = driver.find_element('class',' ytp-large-play-button ytp-button ytp-large-play-button-red-bg').click()
        # driver.switch_to.default_content()


        
    elif 'exit' in voice:
        speak('Goodbye Master!')
        driver.quit()
        break
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(0)
  