from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from utilities.handy_wrappers import HandyWrappers


class DynamicXPathFormat():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


       # Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("erikaqatest0031@mailinator.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("Passw0rd!")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")

        # Select Course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()





ff = DynamicXPathFormat()
ff.test()