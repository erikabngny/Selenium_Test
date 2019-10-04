from selenium import webdriver


class BrowserInteraction():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)

        # Window Maximize
        driver.maximize_window()
        # Open the URL
        driver.get(baseURL)
        # Get Title
        title = driver.title

        print("Title of the web page is: " + title)
        # Get Current URL
        currentUrl = driver.current_url
        print("Current URL of the web page is: " + currentUrl)
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another URL
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        currentUrl = driver.current_url
        print("Current URL again of the web page is: " + currentUrl)
        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        # Get Page Source
        pageSource = driver.page_source
        print(pageSource)
        # Browser Close/Quit
        driver.quit()

ff = BrowserInteraction()
ff.test()