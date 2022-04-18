from selenium.webdriver.common.by import By

#-- Golden rule: Locators of the same page belong to the same class.

class MainPageLocators(object):
  GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
  pass