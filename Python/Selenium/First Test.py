import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://selenium.dev")

# To open the browser full screen:
driver.maximize_window()

title = driver.title   # to capture the title
print(title)

# to verify that the page has "Selenium" in the title
assert "Selenium" in title  # verify: expected value vs. actual value

# find locator
driver.find_element(By.)


# Keep the browser open for 10 seconds before closing
time.sleep(10)

# Optionally, you can close the browser manually or automate it at the end
browser.quit()

# ELEMENTS
# - are HTML elements : anything like buttons, input fields, names:
# Checkboxes, Links, Text Fields, etc.

# LOCATORS
# - mechanisms / techniques to use to indentify and locate these web elements
#Types of locators (8 types):
# ID, Name, Class Name, CSS Selector, Xpath, Link Text, Partial Link Text, Tag Name

# INTERACTIONS
# Examples:
# - Text Field (typing something),
# - Checkbox (checking the checkbox),
# - Link (clicking on a link)

# ASSERTIONS
# Examples:
# - Verify the functionality,
# - Verify that there should be a button with a text "Login"

# Selectorshub