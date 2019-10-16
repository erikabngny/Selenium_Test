import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebsite1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def getNavNames(self):
        # Get navigation names
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.implicitly_wait(3)

        contact = driver.find_element(By.ID, "contact-link")
        contactName = contact.text
        print("Contact Link Name is: " + contactName)

        signin = driver.find_element(By.XPATH, "//a[@class='login']")
        signinName = signin.text
        print("Signin Link Name is: " + signinName)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
