import time

from selenium import webdriver

username = "admin"
password = "admin"

# to access the authentification pop-up, append username and password to the url
# https://username:password@domain/path
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"

browser = webdriver.Chrome()
browser.maximize_window()

time.sleep(4)
browser.get(url)

time.sleep(2)