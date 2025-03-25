from selenium import webdriver

username = "admin"
password = "admin"

# to access the authentication pop-up, append username and password to the URL
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

browser = webdriver.Chrome()
browser.maximize_window()

time.sleep(4)
browser.get(url)

time.sleep(2)