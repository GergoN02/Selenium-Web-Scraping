# Selenium Web Scraping tutorial

# Chromium Web Driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "C:\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(DRIVER_PATH, options=options)

# Website to Scrape
driver.get("https://www.nasdaq.com/market-activity/stocks")

cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_accept.click()


main_search = driver.find_element(By.ID, "find-symbol-input-dark")

if main_search:
    main_search.send_keys("TSLA")
    main_search.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]")))
        print(element.text)

    except:
        print("OOF")

else:
    print("Error, no searchbox found")
