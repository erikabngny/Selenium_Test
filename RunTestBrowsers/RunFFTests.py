from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()