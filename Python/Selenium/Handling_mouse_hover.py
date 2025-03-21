from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

time.sleep(4)
#Creating Action Chain Objects:
actions = ActionChains(browser)
hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()    # you need .perform() to perform the hover action
# .move_to_element is just moving the mouse to the located element, but .perform() is needed to trigger hover action
time.sleep(2)

browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()

time.sleep(2)