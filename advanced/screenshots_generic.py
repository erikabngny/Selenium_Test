from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots():

    def test(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "//*[@id='navbar']//a[@href = '/sign_in']").click()
        time.sleep(2)
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)
        # destinationFileName = "/Users/erikabonganay/Desktop/test.png"



    def takeScreenshot(self, driver):

        filename = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/Users/erikabonganay/Desktop/"
        destinationFile = screenshotDirectory + filename

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.test()
