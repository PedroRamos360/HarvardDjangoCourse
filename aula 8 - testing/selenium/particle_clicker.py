from selenium import webdriver
import keyboard 


driver = webdriver.Chrome()

uri = 'https://particle-clicker.web.cern.ch/'

driver.get(uri)

particle = driver.find_element_by_id('detector-events')

while True:
    particle.click()
    if keyboard.is_pressed('q'): 
        input('Clique enter para continuar')

