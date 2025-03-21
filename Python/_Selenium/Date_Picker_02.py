from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

time.sleep(4)

date_picker = browser.find_element(By.ID, 'datepicker2')
date_picker.click()

time.sleep(1)

current_day = datetime.now()
print(current_day)

next_day = current_day + timedelta(days=1)
print(next_day)
Next_day = (str(next_day.day))
print(Next_day)

current_month = current_day.month
current_year = current_day.year

next_month = (current_month % 12) + 1
next_year = current_year + 1
next_month_year = f"{next_month}/{current_year}"

# Selecting value from the "Month" dropdown menu:
Month_Dropdown = browser.find_element(By.CSS_SELECTOR, 'select[title="Change the month"]')
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))

time.sleep(1)

# Selecting value from the"Year" dropdown menu:
Year_Dropdown = browser.find_element(By.CSS_SELECTOR, 'select[title="Change the year"]')
select = Select(Year_Dropdown)
select.select_by_visible_text(f"{next_year}")

time.sleep(1)

browser.find_element(By.LINK_TEXT, Next_day).click()

time.sleep(2)