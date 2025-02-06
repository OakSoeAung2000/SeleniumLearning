from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")