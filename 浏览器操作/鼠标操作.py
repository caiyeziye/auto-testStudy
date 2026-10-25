
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('http://localhost:63342/autoTest/testA.html?_ijt=6vk4n80rdd12fblmj9ch63f824&_ij_reload=RELOAD_ON_SAVE')
username = driver.find_element(By.ID, 'username')
loginBtn = driver.find_element(By.ID, 'loginBtn')
linktext = driver.find_element(By.ID, 'search')
sleep(1)
actions = ActionChains(driver)
#右键单击
# actions.context_click(username).perform()
# sleep(1)
#左键双击
# actions.double_click(loginBtn).perform()
# sleep(1)
#鼠标左键将一个组件拖动到另一个主键
# actions.drag_and_drop(linktext,username).perform()
# sleep(1)
#将设备移动到控件上方悬停
actions.move_to_element(loginBtn).perform()
sleep(1)
driver.quit()