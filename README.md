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

