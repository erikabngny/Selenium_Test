from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.explicit_wait_type import ExplicitWaitType


class CalendarSelection():

    def test(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(.5)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        departingField = driver.find_element(By.ID, "flight-departing-hp-flight").click()
        dateToSelect = driver.find_element(By.XPATH,"//div[@class='datepicker-cal-month'][position()=1]//button[@data-day='11']")

        time.sleep(5)
        driver.quit()

    def test2(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(.5)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        departingField = driver.find_element(By.ID, "flight-departing-hp-flight").click()
        calMonth = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        allValidDate = calMonth.find_elements(By.TAG_NAME, "button")

        for date in allValidDate:
            if date.text == "October 31":
                date.click()
                break


ff = CalendarSelection()
ff.test2()
