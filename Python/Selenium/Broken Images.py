from http.client import responses  # Import responses from http.client to handle HTTP status codes if needed

import requests  # Import the requests library to send HTTP requests and check image status
from selenium import webdriver  # Import the webdriver module to control the browser via Selenium
from selenium.webdriver.common.by import By  # Import By to locate elements in the browser

# Initialize the Chrome browser using Selenium
browser = webdriver.Chrome()

# Open the target webpage containing images to check
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()  # Maximize the browser window to ensure all images are visible

# Find all image elements on the page using their tag name "img"
images = browser.find_elements(By.TAG_NAME, "img")

# Create an empty list to store the sources of broken images
broken_images = []

# Loop through all found image elements
for image in images:
    src = image.get_attribute("src")  # Get the source URL of the image
    if src:  # If the image has a source URL
        response = requests.get(src)  # Send a GET request to the image URL to check its status
        if response.status_code != 200:  # If the status code is not 200 (OK), the image is broken
            broken_images.append(src)  # Add the broken image URL to the broken_images list
            print(f"Broken image found")  # Print a message indicating a broken image

# If there are broken images found, print the list of broken images
if broken_images:
    print("List of broken images:")
    for broken_image in broken_images:
        print(broken_image)  # Print the URL of each broken image
else:
    print("No broken images found.")  # Print a message if no broken images were found
