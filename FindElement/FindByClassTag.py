from selenium import webdriver


class FindByClassTag():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementByClassName= driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing The Element")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")


        if elementByTagName is not None:
            print("We found an element by Tag Name")




ff = FindByClassTag()
ff.test()