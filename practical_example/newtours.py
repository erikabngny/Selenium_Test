from selenium import webdriver
import unittest


# Check if the title of Newtours Page is "Welcome: Mercury Tours"

class NewTours(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/index.php")
        driver.implicitly_wait(3)

        actualTitle = driver.title
        expectedTitle = "Welcome: Mercury Tours"
        self.assertEqual(actualTitle, expectedTitle, "Actual Title is not equal to Expected Title")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
