# Optionally, to add some time before closing the Chrome window:
import time

# main section:
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://selenium.dev/')

# Keep the browser open for 10 seconds before closing
time.sleep(10)

# Optionally, you can close the browser manually or automate it at the end
driver.quit()