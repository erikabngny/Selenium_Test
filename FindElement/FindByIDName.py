from selenium import webdriver


class FindByIDName():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementById = driver.find_elements_by_id("name")

        if elementById is not None:
            print("We found an element by ID")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")




ff = FindByIDName()
ff.test()