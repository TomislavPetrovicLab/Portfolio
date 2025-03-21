import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://demo.automationtesting.in/Resizable.html"
browser.maximize_window()

browser.get(url)

resizeable_element = browser.find_element(By.XPATH, "//div[contains(@class, 'ui-resizable-handle') and contains(@class, 'ui-resizable-se')]")
Initial_element_size = browser.find_element(By.XPATH, "//div[contains(@class, 'ui-widget-content') and contains(@class, 'ui-resizable')]")

initial_size = Initial_element_size.size
print("Initial size:", initial_size)

time.sleep(4)

action_chains = ActionChains(browser)
action_chains.click_and_hold(resizeable_element).move_by_offset(xoffset=500, yoffset=500).pause(1).release().perform()

time.sleep(2)

resized_element = Initial_element_size.size
print("Resized Element size:", resized_element)

time.sleep(2)
browser.quit()