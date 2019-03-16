class Loginpage1:
    def __init__(self, driver):
        self.driver = driver
        self.unlocator = 'j_username'
        self.unpassword = 'j_password'

    def enter_username(self):
        self.driver.find_element_by_id("j_username").send_keys("admin")

    def enter_password(self):
        self.driver.find_element_by_name(self.unpassword).send_keys("manager")
