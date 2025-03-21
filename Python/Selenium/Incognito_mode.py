import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options

url = "https://www.google.com/"

chrome_options = Options()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get(url)

time.sleep(4)

# firefox_options = Options()
# firefox_options.add_argument("--private")

# browser = webdriver.Firefox(options=firefox_options)
# browser.maximize_window()

# browser.get(url)

# time.sleep(4)
