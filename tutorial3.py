# Selenium Tutorial #3 - Page Navigating and Clicking Elements

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = '/Users/ducnguyen/Programs/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.techwithtim.net')

#-- Click on 'Python Programming'
#-- Find the text that shown up for a link and use that to access the element
link = driver.find_element_by_link_text('Python Programming')
#-- Click on the link
link.click()

try:
  #-- Click on 'Beginner Python Tutorials'
  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
  )
  element.click()

  #-- Click on 'Get Started' button
  element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ow-icon-placement-right ow-button-hover'))
    # EC.presence_of_element_located((By.ID, 'sow-button-19310003'))
  )
  #-- Because the sample page have ads, so clicking on the button doesn't work
  #-- So just learn the code and test it somewhere else
  element.click()

  #-- Go back to Home page (go back to the previous page 3x)
  driver.back()
  driver.back()
  driver.back()

  #-- Go forward
  driver.forward()

except:
  driver.quit()
# except Exception as e:
#     print(e)
