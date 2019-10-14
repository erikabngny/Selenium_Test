from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavascriptExecution():

    def test(self):
        # baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        #driver.get(baseURL)
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice'; ")
        driver.implicitly_wait(3)

        #element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


ff = JavascriptExecution()
ff.test()
