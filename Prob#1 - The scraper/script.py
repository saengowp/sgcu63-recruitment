"""
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
   Download it and replace the `driverpath` variable with the file's path
3. Use pip to install `selenium` and `Jinja2` (see requirements.txt)


Usage
--------------------

`python script.py`

"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from jinja2 import Template
from pathlib import Path

driverpath = 'chromedriver'
targeturl = 'https://rubnongkaomai.com/baan/'

class IndexPage:
    """ A class representing interaction with the baan list page """

    def __init__(self, driver):
        self.driver = driver

    def __activatetabpane(self):
        """ A helper method that clicks all the baan categories to load them """

        tabs = self.driver.find_elements(By.CSS_SELECTOR, ".ant-tabs-nav .ant-tabs-tab")
        print("index: clicking baan size selection buttons: " + ', '.join(t.text for t in tabs))
        for t in tabs:
            t.click()

    def baannamelist(self):
        """ Return list of baan's id """

        baanList = []

        print("index: retrieving baan list")
        self.driver.get(targeturl)
        self.__activatetabpane()
        hyperlinkElement = self.driver.find_elements(By.TAG_NAME, 'a')
        for element in hyperlinkElement:
            hrefAttr = element.get_attribute('href')
            if hrefAttr == None:
                continue
            if not hrefAttr.startswith(targeturl):
                continue
            baanName = hrefAttr[len(targeturl):]
            baanList.append(baanName)

        print("index: found {} entries".format(len(baanList)))
        return baanList


class BaanPage:
    """ Represent interaction with each baan's page """

    def __init__(self, driver, baanid):
        self.driver = driver
        self.baanid = baanid

    def data(self):
        """ Return dict of name and slogan for this baan """
        print("baan: visiting " + self.baanid)
        self.driver.get(targeturl + self.baanid)
        name = self.driver.find_element(By.CSS_SELECTOR, "div > h1[type='header']").text
        slogan = self.driver.find_element(By.CSS_SELECTOR, "div > h3[type='header']").get_attribute("innerHTML")
        return {"name": name, "slogan": slogan}


def exportHtml(baandata):
    """ export baan data to table.html """

    template = Template(Path("template.html").read_text())
    print("exporthtml: Exporting data to table.html")
    result = template.render(data = baandata)
    with open("table.html", "w") as f:
        f.write(result)


print("driver: starting chromium")
with Chrome(executable_path=driverpath) as driver:
    index = IndexPage(driver)
    baannames = index.baannamelist()
    baandata = [BaanPage(driver, name).data() for name in baannames]
    exportHtml(baandata)
    print("task completed")
