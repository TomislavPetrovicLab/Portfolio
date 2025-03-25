from selenium import webdriver

username = "admin"
password = "admin"

# to access the authentication pop-up, append username and password to the URL
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

browser = webdriver.Chrome()
browser.maximize_window()

# Use implicit wait instead of time.sleep()
browser.implicitly_wait(5)  # Waits up to 5 seconds for elements to be found

browser.get(url)

time.sleep(2)