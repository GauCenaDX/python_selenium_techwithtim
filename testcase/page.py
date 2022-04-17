#-- This will be the based class for all our pages
class BasePage(object):
  def __init__(self, driver):
    self.driver = driver

#-- Define a class for each page we want to test (using Base Inheritance)
class MainPage(BasePage):

  #-- A method to check if the title of the page matches with what we want it
  #--   to show - is the word 'Python' appear in the title of the page
  def is_title_matches(self):
    return 'Python' in self.driver.title

  def click_go_button(self):
    element = self.driver.find_element()
    element.click()