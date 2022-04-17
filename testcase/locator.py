from selenium.webdriver.common.by import By

#-- Golden rule: Locators of the same page belong to the same class.

#-- Make a class to define all the locators for the Main Page
class MainPageLocators(object):
  #-- To access an element: by which attribute, what is the value of that attribute
  #-- CAPITALIZED for constant
  GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
  #-- A class for search results locators. All search results locators should
  #--   come here.
  pass