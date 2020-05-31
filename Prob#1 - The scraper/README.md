Data scraper for retrieving rubnongkaomai baan's slogans
====================

This file is a scraper script for retrieving baan's slogans. It retrieves the data by using selenium to simulate
user's interaction of browsing each baan. It then export the result to `table.html`. The simulated process are:

1. Browse rubnongkaomai.com/baan/ .
2. Click all the baan categories tab on the left side to load all the baan.
3. Extract all baan's url
4. Visit all baan's url and extract the baan's name and slogan


Prerequisite
--------------------
1. Install Chromium browser
2. Download Chromium Selenium driver: https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/
   Download it and replate `driverpath` with the file's path
3. Use pip to install `selenium` and `Jinja2` (see requirements.txt)


Usage
--------------------

`python script.py`

