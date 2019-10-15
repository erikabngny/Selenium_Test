from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class PythonSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
