from selenium.webdriver.common.by import By


class testpage:
    def __init__(self, driver):
        self.driverelement = driver

    def Username(self, Username):
        self.driverelement.find_element(By.NAME, 'username').send_keys(Username)

    def Password(self, Password):
        self.driverelement.find_element(By.NAME, 'password').send_keys(Password)

    def button(self):
        self.driverelement.find_element(By.XPATH, "//button[@type='submit']").click()