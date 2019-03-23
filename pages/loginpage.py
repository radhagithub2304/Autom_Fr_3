from testdata.data import *
class Loginpage1:
    def __init__(self, driver):
        self.driver = driver
        self.unlocator = 'j_username'
        self.unpassword = 'j_password'
        self.unsubmit='Submit'

    def enter_username(self):
        self.driver.find_element_by_id(self.unlocator).send_keys(UN)

    def enter_password(self):
        self.driver.find_element_by_name(self.unpassword).send_keys(PWD)

    def submit_login(self):
        self.driver.find_element_by_name(self.unsubmit).click()
