from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')

driver.find_element(By.ID, 'username').send_keys('123')
driver.find_element(By.ID, 'password').send_keys('123456')
sleep(3)
driver.find_element(By.ID, 'username').clear()
driver.find_element(By.ID, 'username').send_keys('admin')
sleep(3)
driver.find_element(By.ID, 'loginBtn').click()
sleep(3)
driver.quit()