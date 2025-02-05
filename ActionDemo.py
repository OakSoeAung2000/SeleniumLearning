from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.click_and_hold()
# action.double_click(driver.find_element(By.))
# action.context_click()
#action.drag_and_drop()
