class Homepage1:
    def __init__(self, driver):
        # pass driver as argument bec driver is defined in test file
        self.driver = driver
        self.unlogout = "//b[text()='log out']"

    def user_logout(self):
        self.driver.find_element_by_xpath(self.unlogout).click()


