# Selenium Tutorial #1

#-- Import webdriver from selenium
from selenium import webdriver

#-- Provide path to ChromeDriver
PATH = '/Users/ducnguyen/Programs/chromedriver'

#-- Select the driver we want to use, and specify the webdriver 
#-- for this web browser
driver = webdriver.Chrome(PATH)

#-- Open a website
driver.get('https://www.google.com')

#-- To get the title of the website
print(driver.title)

#-- To close the current tab of the browser
# driver.close()

#-- To close the entire browser
# driver.quit()