from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


browser = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker"
browser.get(url)
browser.maximize_window()

# It takes time to load close button
time.sleep(4)   # added time to load the close button

close_button = browser.find_element(By.XPATH, '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]').click()

time.sleep(4)

frameLo = browser.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frameLo)
date_picker = browser.find_element(By.CSS_SELECTOR, '#datepicker')
date_picker.click()

current_date = datetime.now()

next_date = current_date + timedelta(days=0)

formatted_date = next_date.strftime("%m/%d/%y")         # defining the date format

date_picker.send_keys(formatted_date + Keys.TAB)

time.sleep(4)

browser.quit()



# Another way: WebDriverWait + Expected conditions + Cookies modal window close
#  ---treba ga prilagoditi - ne funkcionira---
# wait = WebDriverWait(browser, 10)  # Čekamo max 10 sekundi

# **Zatvaranje Cookie modalnog prozora ako se pojavi**
# try:
#     cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "accept-choices")))  # Pronađi dugme za prihvaćanje cookieja
#     cookie_button.click()
#     print("Cookie modal zatvoren!")
# except Exception as e:
#     print("Cookie modal nije pronađen ili nije bilo potrebno zatvoriti ga:", str(e))

# **Čekamo da overlay nestane**
# try:
#     wait.until(EC.invisibility_of_element((By.CLASS_NAME, "fc-dialog-overlay")))
#     print("Overlay nestao.")
# except Exception as e:
#     print("Nema overlaya ili nije nestao:", str(e))

# **Čekamo i klikamo na 'close_img'**
# try:
#     close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="close_img"]')))
#     close_button.click()
#     print("Close button kliknut!")
# except Exception as e:
#     print("Close button nije pronađen ili nije klikabilan:", str(e))

# **Prebacivanje u iframe i klikanje na datepicker**
# try:
#     frameLo = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame lazyloaded']")))
#     browser.switch_to.frame(frameLo)
#     datepicker = wait.until(EC.element_to_be_clickable((By.ID, "datepicker")))
#     datepicker.click()
#     print("Datepicker kliknut!")
# except Exception as e:
#     print("Greška s datepickerom:", str(e))

# browser.quit()