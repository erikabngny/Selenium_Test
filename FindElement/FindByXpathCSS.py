from selenium import webdriver


class FindByXpathCSS():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementByXpath= driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByCSS = driver.find_element_by_css_selector("[placeholder='Hide\/Show Example']")

        if elementByCSS is not None:
            print("We found an element by CSS")




ff = FindByXpathCSS()
ff.test()