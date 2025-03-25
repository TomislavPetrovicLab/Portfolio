import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

with open('saucedemo_test_data_Sheet1.json', 'r') as file:
    test_data = json.load(file)

url = 'https://www.saucedemo.com/'

for data in test_data['users_for_saucedemo']:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    time.sleep(4)
    browser.find_element(By.ID, "user-name").send_keys(data['username'])
    browser.find_element(By.ID, "password").send_keys(data['password'])
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)
    browser.quit()
