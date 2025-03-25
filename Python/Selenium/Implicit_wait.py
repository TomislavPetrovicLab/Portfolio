from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)     # dynamic wait for max. 10s for each element to load
browser.maximize_window()

url = "https://www.saucedemo.com/"
browser.get(url)

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
browser.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click()

browser.quit()