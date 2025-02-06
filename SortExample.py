from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("headless")
# chrome_option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5)
sortedList = []


driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    sortedList.append(ele.text)
originalSorted = sortedList.copy()

sortedList.sort()

assert sortedList == originalSorted
print(sortedList)
