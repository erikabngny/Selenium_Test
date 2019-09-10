from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        elementByLinkText= driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link text")




ff = FindByLinkText()
ff.test()