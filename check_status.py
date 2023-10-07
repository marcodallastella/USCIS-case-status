import os
import random
import time
import csv
from datetime import datetime
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    MoveTargetOutOfBoundsException,
    TimeoutException,
    WebDriverException,
)

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

def open_browser():
    """
    Opens a new automated browser window with all tell-tales of automated browser disabled
    """
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("-headless")  # Enable headless mode
    
    # Remove all signs of this being an automated browser
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    options.set_preference("marionette.enabled", True)

    # Open the browser with the new options
    driver = Firefox(options=options)
    return driver

driver = open_browser()
time.sleep(3)

print('going to the url')
url = 'https://egov.uscis.gov/'
driver.get(url)
time.sleep(5)

search_box = driver.find_element(
    By.XPATH, 
    '//*[@id="receipt_number"]'
)
search_box

print('sending keys')
search_term = 'EAC2400450864'
search_box.send_keys(search_term)
time.sleep(5)

case_status_box = driver.find_element(
    By.XPATH,
    '/html/body/div/div/main/div/div/div/div[1]/div[1]/button')

case_status_box.click()

def press_enter(driver):
    """
    Sends the ENTER to a webdriver instance.
    """
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
#     actions.perform()
    
    
time.sleep(1)
    
press_enter(driver)

time.sleep(3)

status_section = driver.find_element(
    By.XPATH, 
    '/html/body/div/div/main/div/div/div/div[1]/div[1]/div[1]'
)

time.sleep(2)

status = status_section.find_element(
    By.TAG_NAME, 'h2'
    ).text

print(f'Status found: {status}')

time.sleep(2)

description = status_section.find_element(
    By.TAG_NAME, 'p'
    ).text

print(f'Description found: {description}')

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Check if the file "status_check.csv" exists
# file_exists = os.path.isfile("status_check.csv")

# # Create and open the CSV file for writing
# with open("status_check.csv", mode="a", newline="") as file:
#     fieldnames = ["Timestamp", "Status", "Description"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     # If the file doesn't exist, write the header row
#     if not file_exists:
#         writer.writeheader()

#     # Write the data to the CSV file
#     writer.writerow({"Timestamp": timestamp, "Status": status, "Description": description})


# Close the WebDriver
driver.quit()

# Create a dictionary with the data
data_dict = {
    'Timestamp': [timestamp],
    'Status': [status],
    'Description': [description]
}

# Create a DataFrame from the dictionary
data = pd.DataFrame(data_dict)

data

# Append the data to the existing CSV file (mode='a' for append)
data.to_csv('status_check.csv', mode='a', header=False, index=False)
