from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class GetAttribute():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("type")




        print("Value of Attribute is: " + result)
        time.sleep(2)
        driver.quit()

ff = GetAttribute()
ff.test()