import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

endpoint = "https://www.nseindia.com/market-data/securities-available-for-trading"


def download_equity_segment_csv_file(endpoint):
    driver_path = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=driver_path, options=options)
    driver.get(endpoint)
    csv = driver.find_element(By.LINK_TEXT, 'Securities available for Equity segment (.csv)')
    csv.click()
    time.sleep(5)
    driver.quit()


download_equity_segment_csv_file(endpoint=endpoint)
