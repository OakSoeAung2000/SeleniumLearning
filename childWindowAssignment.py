import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase.fixtures.page_actions import click

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
changeWin = driver.window_handles

driver.switch_to.window(changeWin[1])
usern = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(changeWin[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(usern)
driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("123")
driver.find_element(By.CSS_SELECTOR, ".customradio").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()





