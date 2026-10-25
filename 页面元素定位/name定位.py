from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6almv0tsl3nnsuop058fv3t1on&_ij_reload=RELOAD_ON_SAVE')
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('admin')
password.send_keys('123456')
driver.find_element(By.ID,'loginBtn').click()
sleep(3)
driver.quit()