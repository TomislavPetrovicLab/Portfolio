import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = driver.get("https://openjsf.org/cla")

all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total number of links on the page: {len(all_links)}")

for link in all_links:
    href = link.get_attribute("href")  # Get the href attribute
    if href:  # Ensure href is not None or empty
        try:
            response = requests.get(href, timeout=5)  # Add timeout to avoid hanging
            if response.status_code >= 400:
                print(f"Broken link: {href} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error checking link {href}: {e}")

driver.quit()


