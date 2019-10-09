from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from utilities.handy_wrappers import HandyWrappers


class ImplicitWaitDemo():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")





ff = ImplicitWaitDemo()
ff.test()