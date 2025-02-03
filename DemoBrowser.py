import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("oak@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(1)
dropdown.select_by_visible_text('Female')
driver.find_element(By.XPATH, "//input[@type='submit']").click()



message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hellow")

time.sleep(10)