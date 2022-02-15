from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime

DRIVER_PATH = Service("C:\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=DRIVER_PATH, options=options)

# Spreadsheet Setup

CSV_PATH = 'Stocks_test.csv'

# Initialize a pandas DataFramen and read the spreadsheet values
df = pd.read_csv(CSV_PATH)

# OR for Excel Sheets:
# df = pd.read_excel('file_name.xlsx', sheet_name='Sheet1')

# Create an array of all items in the Stocks column
stocks_list = df['Stocks'].tolist()
print(stocks_list)

values = []
time_checked = []

# The output DataFrame is constructed from a dictionary (kind of like a hash table) here
frame_dict = {'Stocks': stocks_list,
              'Value': values, 'Time Checked': time_checked}


# Website to Scrape
driver.get("https://www.nasdaq.com/market-activity/stocks/tsla")

cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_accept.click()

# Do this for every stock
for stock in stocks_list:
    main_search = driver.find_element(By.ID, "find-symbol-input")

    if main_search:
        main_search.send_keys(stock)
        main_search.send_keys(Keys.RETURN)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]")))
            print(element.text)
            values.append(element.text)
            time_checked.append(datetime.now())

        except:
            print("Stock or Value not found")
            values.append("ERROR")
            time_checked.append(datetime.now())

    else:
        print("Search Error")

# Write results to CSV file

# Construct the output DataFrame from our dictionary
df_out = pd.DataFrame(frame_dict)

df_out.to_csv(CSV_PATH)

# Close the webdriver instance
driver.quit()
