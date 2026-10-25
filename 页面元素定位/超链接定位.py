from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
sleep(2)
driver.find_element(By.LINK_TEXT, '百度一下，你就知道').click()
sleep(2)

driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, '你就知道').click()
sleep(2)
driver.quit()