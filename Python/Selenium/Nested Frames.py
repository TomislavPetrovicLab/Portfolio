from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')

browser.switch_to.frame("frame-top")        # Switching to the top frame

browser.switch_to.frame("frame-middle")     # Switching to the middle frame

content_middle = browser.find_element(By.ID, 'content').text
print("Content in middle frame:", content_middle)
# print(f'Content in the middle frame: {content}')      # other way to print the text value

browser.switch_to.default_content()         # Switch to default content

browser.switch_to.frame('frame-bottom')    # Switch to the bottom frame
content_bottom = browser.find_element(By.TAG_NAME, 'body').text
print("Content in bottom frame:", content_bottom)

time.sleep(2)