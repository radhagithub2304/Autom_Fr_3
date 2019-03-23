import time
from pages.loginpage import Loginpage1
from selenium import webdriver


def test_launch_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/manage")
    driver.maximize_window()
    driver.implicitly_wait(10)


def test_login():
    # driver.find_element_by_id("j_username").send_keys("admin")
    lp = Loginpage1(driver)
    lp.enter_username()
    lp.enter_password()

    # driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()


def test_logout():
    time.sleep(5)
    driver.find_element_by_xpath("//b[text()='log out']").click()
