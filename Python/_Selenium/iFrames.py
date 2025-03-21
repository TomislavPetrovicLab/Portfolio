from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Frames.html")

iframe = browser.find_element(By.ID, "singleframe")
browser.switch_to.frame(iframe)

Text_editor = browser.find_element(By.XPATH, '//input[@type="text"]')
Text_editor.clear()
Text_editor.send_keys("I am going to find a job in Austria as QA tester/engineer.")

time.sleep(4)

browser.switch_to.default_content()
browser.find_element(By.XPATH, '//a[@class="link facebook"]').click()

time.sleep(4)