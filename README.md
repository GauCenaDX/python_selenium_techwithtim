# Python Selenium Tutorial

Author: Tech with Tim  
Date: Apr 26, 2020  

Started: Apr 15, 2022  
End: TBU  

This is a code along session from a YouTube tutorial by Tech with Tim:
https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ  


## 01 Web Scraping, Bots & Testing

1. Make sure pip is installed
  - pip comes with Python
  - To check if we have pip
    - In windows: $ pip
    - In Linux or Mac: $ pip3
  - If encounter problem, this video will show how to fix pip:
    https://www.youtube.com/watch?v=AdUZArA-kZw
2. Install selenium
  - Update pip:
    > pip3 install --upgrade pip
  - Install selenium
    > $ pip3 install selenium
3. Download and install ChromeDriver (WebDriver for Chrome)
  - Check which version of Chrome Browser that we have
    > Go to Hamburger menu -> help -> About Chrome  
    >
    > Example: Version 100.0.4896.127 (Official Build) (arm64)
  - Download the correct chrome driver:
    > Go to https://chromedriver.chromium.org/downloads  
    > For Chrome version 100, download ChromeDriver 100.0.4896.60  
    > Download the correct installation for our operating system  
    > Unzip and move the chromedriver.exe to a directory. Remember the path so we can reference this file in our code
  - Notes: If you face “Error: “chromedriver” cannot be opened because the developer cannot be verified. Unable to launch the chrome browser“, you need to go to the chromedriver directory and right-click chromeDriver file and open it. After this step, re-run your tests, chrome driver will work.

## 02 Locating Elements From HTML

**Goal:** Access the search bar, perform a search and return the results to our Python code.

1. Import 'common keys' from selenium webdriver to deal with things such as 'enter' or 'escape' key
2. Import 'time' to delay program execution
3. Find the HTML element (the search bar) on the website:

  - Right-click on the element and click "inspect" the element

      > Now we will see the HTML element that is used to defined the element  
      >
      > ```<input type="search" class="search-field" placeholder="Search …" value="" name="s">```

  **Note:** The most common ways to access an element are to use id, class or name.(The hierarchy rule is id, name and then class. When using class, the first element we encounter will be selected.
  - Get the search bar element by its name.
  - Give input "test" into the search bar
  - Hit 'enter' to perform the search
4. Get the title of all articles returned from the search
    - Inpsect article element from the result of the search  
        ![alt text][inspect-article-title-img]
    - Use Explicit Wait to hold up Selenium and to have it wait for other result
        https://selenium-python.readthedocs.io/waits.html#explicit-waits
    - Inpsect and find the article summary element  
        ![alt text][inspect_article_summary-img]
    - Get a list of all articles
    - Get the summary of each article by accessing the class 'entry-summary'

## 03 Page Navigating and Clicking Elements

**Goals** How to navigate in a web page: to to click on link, button, or go back to previous page.

1. Go to Home page
2. Click on Python Programming on side bar
3. Click on Beginner Python tutorial
4. Click on Get Started button
  ![alt text][inspect-get-started-img]

**Note:**

Because the sample page have ads, so clicking on the button doesn't work. So just learn the code and test it somewhere else

## 04 ActionChains & Automating Cookie Clicker!

**Goal:** Get access into more advance actions such as drag & drop, double-click, long press, etc.

**Cookie Clicker game website (not active):**
https://orteil.dashnet.org/cookieclicker/

**A very simple game:** click on the cookie as many time as possible until we have enough resources to upgrade the Cursor or Grandma.

![alt text][cookie-clicker-img]

**Read:** Documentation - 7.2 Action Chains
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

Find the id of the cookie image

![alt text][cookie-clicker-cookie-id-img]

Find the id of the number of cookie banner

![alt text][cookie-clicker-numofcookie-img]

Find cursor's price
![alt text][cookie-clicker-cursorprice-img]

Find grandma's price
![alt text][cookie-clicker-grandmaprice-img]

## 05 UnitTest Framework (Part 1)

**Goals:** separate each testing component into class.

**Read:** Selenium Documentation - Page Objects
https://selenium-python.readthedocs.io/page-objects.html

1. Create a folder named 'testcase'
2. Create these files in 'testcase' folder: main.py, element.py, locator.py, page.py
3. Write **setup** procedure and **run** test case in main.py
4. Each page on a website should be written on a separate class in page.py. This is where to write the Selenium code. This will take care of the **logic** of the test.
5. All the code to **locate elements** should be put in locator.py
  - Benefit: easy to keep track and change the IDs or css selectors


[inspect-article-title-img]: image/inspect_article_titles.JPG "inspect article title img"
[inspect_article_summary-img]: image/inspect_article_summary.JPG "inspect article summary img"
[inspect-get-started-img]: image/inspect_get_started_button.JPG "inspect get started button img"

[cookie-clicker-img]: image/cookie-clicker.JPG "cookie clicker img"
[cookie-clicker-cookie-id-img]: image/cookie-clicker-cookieid.JPG "cookie id img"
[cookie-clicker-numofcookie-img]: image/cookie-clicker-numofcookie.JPG "number of cookie img"
[cookie-clicker-cursorprice-img]: image/cookie-clicker-cursorprice.JPG "cursor price img"
[cookie-clicker-grandmaprice-img]: image/cookie-clicker-grandmaprice.JPG "grandma price img"
