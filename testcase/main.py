#-- This version shows how to import test cases from page.py

import unittest
from selenium import webdriver
import page

PATH = '/Users/ducnguyen/Programs/chromedriver'

class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(PATH)
    self.driver.get('https://www.python.org/')

  def test_title(self):
    mainPage = page.MainPage()
    assert mainPage.is_title_matches()

  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main()