from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
username = driver.find_element(By.ID, 'username')
username.send_keys('admin')
print('名字长度:',username.size)
button = driver.find_element(By.ID, 'loginBtn')
print('按钮文本',button.text)

linknote = driver.find_element(By.ID, 'search')
print('链接地址', linknote.get_attribute('href'))

print(username.is_enabled())
print(username.is_displayed())
print(username.is_selected())