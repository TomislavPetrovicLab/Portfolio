# VIEWPORT
# test application on the different screen sizes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)

# driver.set_window_size(768, 1024)

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(2)

finally:
    driver.close()
time.sleep(2)