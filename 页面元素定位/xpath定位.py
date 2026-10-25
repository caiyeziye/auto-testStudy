from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6almv0tsl3nnsuop058fv3t1on&_ij_reload=RELOAD_ON_SAVE')
sleep(1)
# driver.find_element(By.XPATH, '/html/body/div/form/div[1]/input').send_keys('admin')
# driver.find_element(By.XPATH, '/html/body/div/form/div[2]/input').send_keys('123456')
# sleep(1)
# driver.find_element(By.XPATH, '/html/body/div/form/button').click()
# sleep(1)
#
# driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('test')
# sleep(1)
# driver.find_element(By.XPATH, '//button[@id="loginBtn"]').click()
# sleep(1)
# driver.find_element(By.XPATH,'//a[@id="search" and @class="search"]').click()
# sleep(1)

#xpath定位

# driver.find_element(By.XPATH, '//*[@id="loginForm"]//input[@id="username"]').send_keys('admin')
# driver.find_element(By.XPATH, '//*[@id="loginForm"]//input[@id="password"]').send_keys('123456')
# sleep(1)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]//*[@id="loginBtn"]').click()
# sleep(1)
# driver.quit()

#xpath层级定位

driver.find_element(By.XPATH, '//*[contains(@name,"username")]').send_keys('admin')
driver.find_element(By.XPATH, '//*[contains(@name,"password")]').send_keys('123456')
sleep(1)
driver.find_element(By.XPATH, '//*[contains(@id,"loginBtn")]').click()
sleep(1)
driver.find_element(By.XPATH,'//*[text()="百度一下，你就知道"]').click()

driver.quit()