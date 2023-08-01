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

employee_name = driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
employee_name.send_keys('John Antony Cena')
time.sleep(2)

search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()
time.sleep(2)

checkbox = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]")
checkbox.click()
time.sleep(2)

pencil_button = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")
pencil_button.click()
time.sleep(2)

nickname = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
nickname.send_keys('John')
time.sleep(2)

other_id = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
other_id.send_keys('919')
time.sleep(2)

save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()
time.sleep(4)

print("Successfully employee details added")
