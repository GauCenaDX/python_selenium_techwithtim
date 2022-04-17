# Selenium Tutorial #2 - Locating Elements From HTML

from selenium import webdriver
#-- Import common keys to deal with things such as 'enter' or 'escape' key
from selenium.webdriver.common.keys import Keys
#-- For Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-- For timing
import time


PATH = '/Users/ducnguyen/Programs/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.techwithtim.net')
print(driver.title)

#-- 1. Get the search bar element by its name.
#-- 2. Give input "test" into the search bar
#-- 3. Hit 'enter' to perform the search
search = driver.find_element_by_name('s')
#-- Clear the input field
search.clear()
search.send_keys('test')
search.send_keys(Keys.RETURN)

#-- To get the whole page source. This will print a big BLOB on the 
#-- source code of the web page.
# print(driver.page_source)

#-- Use Explicit Wait to hold up Selenium and to have it wait for 'main' element
try:
  #-- This will wait for a maximum of 10 secconds and get the 'main' element 
  #--     for us.
  #-- By.ID can be changed to By.NAME, By.CLASS_NAME, By.TAG_NAME
  main = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, 'main'))
  )

  #-- Get a list of all articles
  articles = main.find_elements_by_tag_name('article')

  #-- Get the summary of each article by accessing the class 'entry-summary'
  for article in articles:
    header = article.find_element_by_class_name('entry-summary')
    print(header.text)

  #-- Sleep for 5 second before quitting the browser
  time.sleep(5)

#-- Change 'finally' to 'except' if we don't want to quit the page
#-- unless there is an error
# except:
finally:
  driver.quit()

#-- Get the 'main' element and print out the text inside of 'main'
# main = driver.find_element_by_id("main")
# print(main.text)