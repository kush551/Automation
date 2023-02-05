from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
username =driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("kush551_")
password = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("sudhir1!shalini")
click = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
click.click()
time.sleep(10)
notnow = driver.find_element(By.XPATH,'//*[@id="mount_0_0_TJ"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div/div[1]/div/div/svg/path')
notnow.click()


time.sleep(100000)
driver.quit()


