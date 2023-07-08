from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
Login = 'standard_user'
Password = 'secret_sauce'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def open_page(driver, URL):
    driver.get(URL)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

def login(driver, name, password):
    element_send_keys(driver, 'user-name', name)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'login-button' )

driver = get_driver()
open_page(driver, URL)
login(driver = driver, name = Login, password = Password)

driver.quit()