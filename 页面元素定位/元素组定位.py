from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6almv0tsl3nnsuop058fv3t1on&_ij_reload=RELOAD_ON_SAVE')
input_group = driver.find_elements(By.TAG_NAME, 'input')
sleep(1)
print(input_group)
input_group[0].send_keys('admin')
input_group[1].send_keys('123456')
sleep(1)
driver.find_element(By.TAG_NAME, 'button').click()
sleep(1)
driver.quit()