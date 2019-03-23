import time
from testdata.data import *
from pages.loginpage import Loginpage1
from pages.Homepage import Homepage1
from selenium import webdriver
import pytest
@pytest.fixture(scope='session')

def test_launch_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(10)


def test_login(test_launch_browser):
    lp=Loginpage1(driver)
    lp.enter_username()
    lp.enter_password()
    lp.submit_login()
    # Above three are reusable components
    # driver.find_element_by_id("j_username").send_keys("admin")
    # driver.find_element_by_name("j_password").send_keys("manager")
    # driver.find_element_by_name("Submit").click()


def test_logout(test_launch_browser):
    time.sleep(10)
    lp1=Homepage1(driver)
    lp1.user_logout()
    # driver.find_element_by_xpath("//b[text()='log out']").click()
