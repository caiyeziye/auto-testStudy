from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('admin')
password.send_keys('123456')
sleep(2)
driver.find_element(By.ID, 'loginBtn').click()
sleep(2)
driver.quit()