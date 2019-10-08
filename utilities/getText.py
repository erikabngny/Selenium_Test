from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class GetText():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element_by_id("opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(2)
        driver.quit()

ff = GetText()
ff.test()