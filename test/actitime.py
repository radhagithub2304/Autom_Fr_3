import time

from selenium import webdriver
def launch_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/manage")
    driver.maximize_window()
    driver.implicitly_wait(10)
def login():
    driver.find_element_by_id("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()
def logout():
    time.sleep(5)
    driver.find_element_by_xpath("//b[text()='log out']").click()
launch_browser()
login()
logout()