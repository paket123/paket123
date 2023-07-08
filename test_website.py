
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#1.Зайти на главную страницу
#2.Открыть страницу login
#3.Заполнить поле email
#4.Заполнить поле пароль
#5.Нажать на кнопку старт

URL = 'https://www.saucedemo.com/'
Login = 'standard_user'
Password = 'secret_sauce'
#1.
driver.get(URL)

#2.
#tut ne nado

#3,4.
input_login = driver.find_element(By.ID,'user-name')
input_password = driver.find_element(By.ID,'password')
input_login.send_keys(Login)
input_password.send_keys(Password)

#5.
register_button = driver.find_element(By.ID,'login-button')
register_button.click()