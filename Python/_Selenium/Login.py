from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"

login_url = "https://www.saucedemo.com/"
driver.get(login_url)

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

time.sleep(1)
username_field.send_keys(username)
time.sleep(1)
password_field.send_keys(password)

time.sleep(1)

login_button = driver.find_element(By.ID, "login-button")

# Check if the button is not disabled - insert assertion:
assert not login_button.get_attribute("disabled")   # verify by getting the attribute

login_button.click()

time.sleep(1)

success_element = driver.find_element(By.CSS_SELECTOR, ".title")
assert success_element.text == "Products"