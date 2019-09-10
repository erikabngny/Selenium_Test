from selenium import webdriver
import os

class RunChromeTests():

    def testMethod(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")

ff = RunChromeTests()
ff.testMethod()