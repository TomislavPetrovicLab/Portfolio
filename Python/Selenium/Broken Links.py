import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL to check for broken links
url = "https://practice-automation.com/broken-links/"

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get(url)

# Wait until the links are loaded (wait for at least one link to be present on the page)
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
all_links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

# Print the total number of links found
print(f"Total number of links on the page: {len(all_links)}")

# Iterate through each link and check if it's broken
for link in all_links:
    href = link.get_attribute("href")
    if href:
        response = requests.get(href)
        if response.status_code >= 400:
            print(f"Broken link: {href}(Status code: {response.status_code})")

# Quit the browser after processing
driver.quit()
