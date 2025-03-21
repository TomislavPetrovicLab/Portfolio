# How to Interact with Dropdown
# How to Use Select Class
# How to Use 3 different methods:
#   - Select by Value, Select by Index, Select by visible text
# How to Count the Dropdown values
# Loop the Dropdown values ("for" loop) and if the desired value found, select that value

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

login_url = "https://the-internet.herokuapp.com/dropdown"   # variable for login webpage
driver.get(login_url)       # to open the webpage that login_url stores as value

time.sleep(2)

dropdown_element = driver.find_element(By.ID, "dropdown")

# To interact with the dropdown - we need to create a select class

# select = Select(dropdown_element)

# 3 different ways to select a dropdown:
#   - Select the value by visible text
#   - Select the value by index
#   - Select the option by using a value

# select.select_by_visible_text("Option 2")
# select.select_by_index(2)
# select.select_by_value("2")


# Test Case: Verify the count of the dropdown values
# dropdown_element = driver.find_element(By.ID, "dropdown")      # Locator: to locate the dropdown menu
# select = Select(dropdown_element)   # to select a dropdown menu
# option_count = len(select.options)  # length of select options

# Asserting the value manually (without tools, e.g., PyTest, UnitTest)
# expected_count = 3  # create a variable to compare it with actual result - variable option_count

# if option_count == expected_count:
#     print("Test case passed. Count is correct.")
# else:
#     print("Test case failed. Count is incorrect.")


# Test Case: Verify that the value "Option 2" is in the dropdown
#   to check all the values in the dropdown, we need to loop them - use "for" loop

target_value = "Option 2"
select = Select(dropdown_element)

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}.")
        break
    else:
        print(f"Option '{target_value}' is not found.")


time.sleep(2)
