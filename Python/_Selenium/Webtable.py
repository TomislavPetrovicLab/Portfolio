from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()

# when locating an element, it's good practice to make it visible on screen:
#   - by automating scrolling through web page till the located element
browser.execute_script("window.scrollTo(0, 700)")
table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(f"Number of rows in table: {row_count}")

target_value = "Australia"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"{target_value} is found")
            break
    if found:
        break

if not found:
    print(f"Target value {target_value} is not found")





time.sleep(2)