# Instagram Commenting Bot

## Dependencies:
- Install Selenium: pip install selenium
- Install chromedriver: Make sure the version you download matches the version of your Chrome browser.
  - Click the 3 dots on the top right corner of your Chrome browser screen > Help > About Google Chrome
  - After it’s downloaded, unzip it and click the executable.
  - Getting “chromedriver cannot be opened” error: you can solve this by going to System Preferences > Security & Privacy > General. Click “open anyway” to open chromedriver.

## Overview: 
- Fill in DRIVER_PATH, POST_URL, USERNAME, PASSWORD variables.
- Chromedriver is used to launch chrome in development mode to test your software
- To simulate a human-like experience, sleep for 90 seconds after each comment in the for loop (40 comments/hour).

## How to use:
- Fill in list of names in handles.txt file
- Remember to fill out variables
- Run the code: python3 ig-comment- bot.py
