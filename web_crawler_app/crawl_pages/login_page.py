from injector import inject, singleton
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@singleton
class LoginPage:
    @inject
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def login(self, username, password):
        self.driver.get('http://extratoclube.com.br/')
        self.driver.switch_to.frame(0)

        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user"))
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "pass"))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "botao"))
        )

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()