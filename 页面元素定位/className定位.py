from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
username = driver.find_element(By.CLASS_NAME, 'username')
password = driver.find_element(By.CLASS_NAME, 'password')
sleep(2)
username.send_keys('admin')
password.send_keys('123456')
driver.find_element(By.ID,'loginBtn').click()
sleep(2)
driver.quit()