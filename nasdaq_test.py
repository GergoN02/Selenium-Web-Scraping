# Selenium Web Scraping tutorial

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For Windows
# DRIVER_PATH = Service("C:\chromedriver.exe")


# For Linux/Mac
DRIVER_PATH = Service("/home/users/your_username/Documents/Selenium_LAB/chromedriver")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=DRIVER_PATH, options=options)

# Website to Scrape
driver.get("https://www.nasdaq.com/market-activity/stocks")

# Locate the Cookie Wall Accept button by ID (as it has one)
cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
# Click the selected button
cookie_accept.click()

# Locate the search box element on the loaded page
main_search = driver.find_element(By.ID, "find-symbol-input-dark")

# Check if element exists, and using the keys module, input text into the search box, then send RETURN for search
if main_search:
    main_search.send_keys("TSLA")
    main_search.send_keys(Keys.RETURN)

    # Using a try-catch block we make sure that the requested page has loaded, and the element we need is accessible by Selenium
    # Print the value of the element to the console
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]")))
        print(element.text)

    except:
        print("OOF")

else:
    print("Error, no searchbox found")
