from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class HiddenElements():

    def testLetsKodeit(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        textBoxElement = driver.find_element_by_id("displayed-text")
        txtbx = textBoxElement.is_displayed()
        print("Text is visible? " + str(txtbx))
        time.sleep(2)

        # Click the Hide Button
        hideButton = driver.find_element_by_id("hide-textbox")
        hideButton.click()

        # Find the state of the text box
        txtbx = textBoxElement.is_displayed()
        print("Text is visible? " + str(txtbx))
        time.sleep(2)

        # Click the Show button
        showButton = driver.find_element_by_id("show-textbox")
        showButton.click()

        # Find the state of the text box
        txtbx = textBoxElement.is_displayed()
        print("Text is visible? " + str(txtbx))
        time.sleep(2)

        # Browser Close
        driver.quit()

        




ff = HiddenElements()
ff.testLetsKodeit()