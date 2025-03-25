from http.client import responses  # Import responses from http.client to handle HTTP status codes if needed

import requests  # Import the requests library to send HTTP requests and check image status
from selenium import webdriver  # Import the webdriver module to control the browser via Selenium
from selenium.webdriver.common.by import By  # Import By to locate elements in the browser

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()
images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []

for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found")
if broken_images:
    print("List of broken images:")
    for broken_image in broken_images:
        print(broken_images)
else:
    print("No broken images found.")