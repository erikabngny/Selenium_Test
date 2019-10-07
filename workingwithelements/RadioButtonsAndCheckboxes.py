from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RadioButtondAndCheckboxes():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()
        
        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected()))
        print("Benz Radio button is selected? " + str(benzRadioBtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz Radio button is selected? " + str(benzCheckbox.is_selected()))


ff = RadioButtondAndCheckboxes()
ff.test()