from selenium import webdriver
from TestPage import testpage
import time


def testcase_01():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)
    TestPage = testpage(driver)
    TestPage.Username('Admin')
    TestPage.Password('invalid123')
    TestPage.button()
    time.sleep(5)