from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
browser.maximize_window()

# to scroll down the website - use javascript
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Check and uncheck a checkbox:
# browser.find_element(By.XPATH, '//label[normalize-space()="Sunday"]').click()
# time.sleep(2)
# browser.find_element(By.XPATH, '//label[normalize-space()="Sunday"]').click()
# time.sleep(2)

# How to check all checkboxes at once
# - need to identify all the checkboxes on the page
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)      # to use space bar to check/uncheck a checkbox
time.sleep(1)

checked_count =0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 7
if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox count mismatch")

browser.close()