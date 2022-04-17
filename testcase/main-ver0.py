#-- Version 0: This version shows how to setup the test environment, define 
#--   methods to run test cases, and run test cases

import unittest
from selenium import webdriver
import page

PATH = '/Users/ducnguyen/Programs/chromedriver'

#-- Create a class inherit from unittest.TestCase
class PythonOrgSearch(unittest.TestCase):

  #-- Run at the beginning. This setup will be run everytime we run a test case
  def setUp(self):
    self.driver = webdriver.Chrome(PATH)
    self.driver.get('https://www.python.org/')

  #-- Method with name start with 'test_' will be run automatically when
  #--   we run the unit test.

  #-- 'assert' will check whether the value on its right side is true

  #-- Test with Failed result
  def test_example(self):
    print('Test')
    assert False

  #-- Test with Pass result
  def test_example2(self):
    print('Test')
    assert True

  def not_a_test(self):
    print('This won\'t print')

  #-- Run at the end
  def tearDown(self):
    self.driver.close()

#-- Run all unit tests that we defined in main
if __name__ == '__main__':
  unittest.main()