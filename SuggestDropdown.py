import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(4)
country = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(country))

for countries in country:
    if countries.text == "India":
        countries.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"