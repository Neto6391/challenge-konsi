from injector import inject, singleton
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio

@singleton
class LoginPage:
    @inject
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.url = 'http://extratoclube.com.br/'

    async def login(self, username, password):
        self.driver.get(self.url)
        self.driver.switch_to.frame(0)

        username_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-container form input#user')
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'div.form-container form input#pass')
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'div.form-container form button#botao')

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    async def perfom_login_async(self, username, password):
        await self.login(username, password)