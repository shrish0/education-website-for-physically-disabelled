from selenium import webdriver
# import StringIO
from PIL import Image 
 
driver = webdriver.Chrome('C:\\xampp\\htdocs\\botedu\\voice-assistant-main')
driver.get('http://localhost/botedu/voice-assistant-main/notes.txt')
 
# screenshot = driver.save_screenshot("botedu\\voice-assistant-main\screenshot\ss.png")

# size = (0, 0, 680, 400)
# image = Image.open("botedu\\voice-assistant-main\screenshot\ss.png")
# image.show()
driver.getText()