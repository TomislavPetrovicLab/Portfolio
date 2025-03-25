from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.saucedemo.com/"
browser.get(url)

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()

wait = WebDriverWait(browser, "10")
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
element.click()

browser.quit()