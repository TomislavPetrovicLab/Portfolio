# BROWSER COMMANDS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximize the browser window
driver.maximize_window()

# Maximize the browser window
driver.minimize_window()

# Expand the browser window to full screen
# driver.fullscreen_window()

# Wait for the "Forgot Password" link to be clickable before clicking it
wait = WebDriverWait(driver, 10)    # Wait for up to 10 seconds
forgot_password_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")))
forgot_password_link.click()


# BROWSER COMMANDS:

# Wait for the back navigation to be complete
wait.until(EC.url_changes(driver.current_url))  # Wait until the URL changes after going back
driver.back()

# Wait for the forward navigation to complete
wait.until(EC.url_changes(driver.current_url))  # Wait until the URL changes after going forward
driver.forward()

# Wait for the page to refresh
driver.refresh()

wait.until(EC.url_changes(driver.current_url))
driver.back()

# Close the browser
driver.close()