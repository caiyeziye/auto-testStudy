from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
sleep(1)
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
sleep(1)
driver.set_window_size(300,300)
sleep(1)
driver.maximize_window()
sleep(1)
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(1)
print(driver.title)
print(driver.current_url)

driver.quit()
