from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


# Check if 'Sign-On' is present

class NewTours(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/index.php")
        driver.implicitly_wait(3)

        time.sleep(10)
        signon = driver.find_element(By.XPATH, "//a[@href='mercurysignon.php']")
        signonText = signon.text
        assert signonText is not None, "Sign On element is not present"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
