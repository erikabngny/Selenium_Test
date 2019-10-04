from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox(executable_path='/Users/erikabonganay/libs/geckodriver.exe')
        driver.get(baseURL)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the List is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Size of the List is: " + str(length2))


ff = ListOfElements()
ff.test()
