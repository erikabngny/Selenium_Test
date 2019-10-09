from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.explicit_wait_type import ExplicitWaitType


class ExplicitWaitDemo2():

    def test(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(.5)

        wait = ExplicitWaitType(driver)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2019")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        returnDate.send_keys("12/26/2019")
        driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']//button[contains(@class, 'btn-primary btn-action gcw-submit')]").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()


ff = ExplicitWaitDemo2()
ff.test()
