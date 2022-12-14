import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

endpoint = "https://www.nseindia.com/all-reports"


def search_for_the_latest_bhavcopy(endpoint):
    driver_path = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=driver_path, options=options)
    driver.get(endpoint)
    searchbox = driver.find_element(By.ID, 'crEquityDailySearch')
    searchbox.click()
    time.sleep(2)
    searchbox.send_keys("Bhavcopy file (csv)")
    download_button = driver.find_elements(By.XPATH, '//*[@id="cr_equity_daily_Current"]/div/div[11]/div/div/span[2]/a')
    download_button[0].click()
    time.sleep(5)
    driver.quit()


def search_for_30_days_report(endpoint):
    driver_path = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=driver_path, options=options)
    driver.get(endpoint)
    monthly_report_tab = driver.find_element(By.XPATH, '//*[@id="cr_equities"]/div/nav/div/a[2]')
    monthly_report_tab.click()
    searchbox = driver.find_element(By.ID, 'crEquityMonSearch')
    searchbox.send_keys('Bhavcopy file (csv)')
    time.sleep(1)
    download_button = driver.find_elements(By.XPATH, '//*[@id="cr_equity_daily_Current"]/div/div[11]/div/div/span[2]/a')
    for i in download_button:
        i.click()
    time.sleep(5)
    driver.quit()


search_for_the_latest_bhavcopy(endpoint=endpoint)
search_for_30_days_report(endpoint=endpoint)