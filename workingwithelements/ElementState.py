from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementState():

    def isEnabled(self):
        baseURL = "https://www.google.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        e1 = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        e1State = e1.is_enabled()
        print("E1 is Enabled? -> " +str(e1State))

        e1.send_keys("letskodeit")


ff = ElementState()
ff.isEnabled()