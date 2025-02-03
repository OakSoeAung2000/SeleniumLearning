import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#
# print(len(checkbox))
#
# for checkboxes in checkbox:
#     if checkboxes.get_attribute("value") == "option2":
#         checkboxes.click()
#         checkboxes.is_selected()
#         break
#
# radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# radiobuttons[2].click()
# assert radiobuttons[2].is_selected()
#
# assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "name").send_keys("Oak")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
AText = alert.text
print(AText)
assert "Oak" in AText
alert.accept()
# alert.dismiss()


time.sleep(10)


