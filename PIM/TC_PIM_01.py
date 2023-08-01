from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
username = driver.find_element(By.NAME, 'username')
username.send_keys('Admin')
password = driver.find_element(By.NAME, 'password')
password.send_keys('admin123')
button = driver.find_element(By.XPATH, "//button[@type='submit']")
button.click()
time.sleep(3)

pim_module_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]")))
pim_module_link.click()
time.sleep(3)

add_employee_button = WebDriverWait(driver, 10).until((EC.visibility_of_element_located((By.XPATH, "(//a[@class='oxd-topbar-body-nav-tab-item'])[2]"))))
add_employee_button.click()
time.sleep(3)

first_name_input = driver.find_element(By.NAME, 'firstName')
first_name_input.send_keys('John')
time.sleep(2)

middle_name_input = driver.find_element(By.NAME, 'middleName')
middle_name_input.send_keys('Antony')
time.sleep(2)

last_name_input = driver.find_element(By.NAME, 'lastName')
last_name_input.send_keys('Cena')
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(5)

print("Added employee successfully")
