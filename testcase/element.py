from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
  #-- For any element that we want to set a value, we must follow this process.
  #-- 'lambda' is anonymous function, 'driver' is an argument of this function.
  #-- 'self.locator' will be equal to the name that we want to use to locate the 
  #--   element. 
  #-- --------------------------
  def __set__(self, obj, value):
    driver = obj.driver
    #-- Wait for the element to exist on the page
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element_by_name(self.locator)
    )
    driver.find_element_by_name(self.locator).clear()
    driver.find_element_by_name(self.locator).send_keys(value)
  #-- --------------------------

  #-- To get the value of an object
  def __get__(self, obj, owner):
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element_by_name(self.locator)
    )
    element = driver.find_element_by_name(self.locator)
    return element.get_attribute('value')