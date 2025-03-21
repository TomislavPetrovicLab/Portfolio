from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"

browser.get(url)
browser.maximize_window()
time.sleep(2)

# JS Alert - Handling:
# Alert_button = browser.find_element(By.XPATH, '//button[normalize-space()="Click for JS Alert"]')
# Alert_button.click()
# alert = browser.switch_to.alert
# alert_text = alert.text
# print(alert_text)
# time.sleep(3)
# alert.accept()
# time.sleep(2)

# JS Confirm - Handling:
# alert_button = browser.find_element(By.XPATH, '//button[normalize-space()="Click for JS Confirm"]')
# time.sleep(2)
# alert_button.click()
# alert_window = browser.switch_to.alert
# alert_text = alert_window.text
# print(alert_text)
# time.sleep(2)

# JS Prompt
browser.find_element(By.XPATH, '//button[normalize-space()="Click for JS Prompt"]').click()
alert_window = browser.switch_to.alert
alert_text = alert_window.text
print(f"Alert text: {alert_text}")
time.sleep(2)
alert_window.send_keys('This is a test case for JS alert.')
time.sleep(2)
alert_window.accept()
time.sleep(2)
