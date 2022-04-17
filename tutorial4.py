# Selenium Tutorial #4 - ActionChains & Automating Cookie Clicker

from selenium import webdriver
#-- import Actions Chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = '/Users/ducnguyen/Programs/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')

#-- Put all products in a list and loop through them to see which product we can upgrade
#-- Code:
#--  . Make a list and load in all elements with id 'productPrice' + 'i'
#--  . i will start at 1 then go to 0 and end at 0
#--  . We try to upgrade the more expensive item first
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range (1,-1-1)]

#-- Create a new ActionChains object that will act on this webdriver
actions = ActionChains(driver)

#-- Store a list of actions (and then perform the actions on the object)
#-- SYNTAX:
#-- actions.click()     -- click wherever the cursor is at
#-- actions.click(obj)  -- click on the object
actions.click(cookie)

#-- perform the actions on the object
for i in range(5000):
  actions.perform()
  #-- 0 cookies per secone : 0
  # count = cookie_count.text
  #-- [0, cookies, per, secone, :, 0] -> get the first element = 0
  count = int(cookie_count.text.split('')[0])
  for item in items:
    value = int(item.text)
    if value <= count:
      upgrade_actions = ActionChains(driver)
      upgrade_actions.move_to_element(item)
      upgrade_actions.click()
      upgrade_actions.perform()
  print(count)
