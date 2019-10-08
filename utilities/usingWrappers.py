from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from utilities.handy_wrappers import HandyWrappers


class UsingWrappers():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)


        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//*[@id='name']", locatorType="xpath")
        textField2.clear()






ff = UsingWrappers()
ff.test()