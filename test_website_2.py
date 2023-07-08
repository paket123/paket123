from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#1.Зайти на главную страницу
#2.Открыть страницу login
#3.Заполнить поле email
#4.Заполнить поле пароль
#5.Нажать на кнопку старт

URL = 'https://www.saucedemo.com/'
Login = 'standard_user'
Password = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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


#1.

driver = get_driver()

open_page(driver, URL)

#2.(ne nujno)

#element_click(driver, 'login-link')
#3,4.
element_send_keys(driver, 'user-name', Login)
element_send_keys(driver, 'password', Password)

#5.
element_click(driver, 'login-button' )