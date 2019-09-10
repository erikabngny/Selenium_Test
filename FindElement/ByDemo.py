from selenium import webdriver
from selenium.webdriver.common.by import By


class ByDemo():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by ID")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by XPath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLinkText is not None:
            print("We found an element by XPath")


ff = ByDemo()
ff.test()