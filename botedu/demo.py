from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3
import subprocess
import wolframalpha
import random
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import datetime 
import json
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import shutil
driver = webdriver.Chrome('C:\\xampp\\htdocs\\botedu\\voice-assistant-main')
driver.maximize_window()
driver.execute_script("window.open('');")
driver.get('http://localhost/botedu/courses.php')
element = driver.find_element('name','Class 10').click()

element = driver.find_element('id','math10').click()
time.sleep(100000000)

