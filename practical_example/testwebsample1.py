import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class TestWebSample1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(3)

    def testMethodNames(self):
        # Get navigation names
        contact = self.driver.find_element(By.ID, "contact-link")
        contactName = contact.text
        print("Contact Link Name is: " + contactName)
        signin = self.driver.find_element(By.XPATH, "//a[@class='login']")
        signinName = signin.text
        print("Signin Link Name is: " + signinName)

    def testMethodClickBlouses(self):
        # Click Blouses and check if Blouses title is present
        driver = self.driver

        try:
            actions = ActionChains(driver)
            womenElement = driver.find_element(By.XPATH, "//a[@title='Women']")
            actions.move_to_element(womenElement).perform()
            print("Mouse Hovered on element")
            time.sleep(10)

            blousesElement = driver.find_element(By.XPATH, "//a[@title='Blouses']")
            blousesElement.click()
            time.sleep(10)
            blousesTitle = driver.find_element(By.XPATH, "/span[@class='category-name']")
            blousesName = blousesTitle.text
            print(blousesName)
            assert blousesName is not None, "Blouses element is not present"
        except:
            print("Mouse Hover failed on element")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
