from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.selenium.dev/')
browser.switch_to.new_window()
browser.get('https://playwright.dev/')

number_of_tabs = len(browser.window_handles)        # to count the number of tabs
print(f"Number of tabs: {number_of_tabs}")
tabs_value = browser.window_handles
print(tabs_value)
Current_tab = browser.current_window_handle
print(Current_tab)
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon")
FirstTab = browser.window_handles[0]

if Current_tab != FirstTab:
    browser.switch_to.window(FirstTab)

browser.find_element(By.XPATH, '//span[normalize-space()="Downloads"]').click()

time.sleep(2)