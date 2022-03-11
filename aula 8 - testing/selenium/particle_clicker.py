from selenium import webdriver
import keyboard 
from time import sleep


driver = webdriver.Chrome()

uri = 'https://particle-clicker.web.cern.ch/'

driver.get(uri)

particle = driver.find_element_by_id('detector-events')

paused = True

def get_paused():
    global paused
    return paused

def set_paused():
    global paused
    if paused == True:
        paused = False
    else:
        paused = True
    return paused

while True:
    paused = get_paused()
    if not paused:
        particle.click()
    if keyboard.is_pressed('p'):
        sleep(.2)
        print(set_paused())


