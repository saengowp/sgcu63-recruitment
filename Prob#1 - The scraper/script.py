from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from jinja2 import Template
from pathlib import Path

driverpath = 'chromedriver/chromedriver'
targeturl = 'https://rubnongkaomai.com/baan/'

class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    def activatetabpane(self):
        tabs = self.driver.find_elements(By.CSS_SELECTOR, ".ant-tabs-nav .ant-tabs-tab")
        print("index: clicking baan size selection buttons: " + ', '.join(t.text for t in tabs))
        for t in tabs:
            t.click()

    def baannamelist(self):
        baanList = []

        print("index: retrieving baan list")
        self.driver.get(targeturl)
        self.activatetabpane()
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

    def __init__(self, driver, baanid):
        self.driver = driver
        self.baanid = baanid

    def data(self):
        print("baan: visiting " + self.baanid)
        self.driver.get(targeturl + self.baanid)
        name = self.driver.find_element(By.CSS_SELECTOR, "div > h1[type='header']").text
        slogan = self.driver.find_element(By.CSS_SELECTOR, "div > h3[type='header']").get_attribute("innerHTML")
        return {"name": name, "slogan": slogan}


def exportHtml(baandata):
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
