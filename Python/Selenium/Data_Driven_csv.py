import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

from Python.Selenium.Incognito_mode import browser


csv_file = 'saucedemo_test_data_Sheet1.csv'

test_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)
print(test_data)

for data in test_data:
    browser = webdriver.Chrome()
    browser.maximize_window()
    url = "https://www.saucedemo.com/"
    browser.get(url)
    time.sleep(5)
    browser.find_element(By.ID, "user-name").send_keys(data['username'])
    browser.find_element(By.ID, "password").send_keys(data['password'])
    browser.find_element(By.ID, "login-button").click()
    time.sleep(2)

browser.quit()