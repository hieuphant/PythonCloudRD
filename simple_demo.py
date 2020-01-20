from selenium import webdriver
from time import sleep

driver = webdriver.Remote( command_executor='http://54.254.166.52:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
driver.get("https://www.google.com/")
sleep(5)
print(driver.title)
driver.quit()