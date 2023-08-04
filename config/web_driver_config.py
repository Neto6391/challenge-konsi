from selenium import webdriver
from injector import Module, singleton
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from config.web_driver_manager import WebDriverManager

class WebDriverConfig(Module):
    def __init__(self, webdriver_manager: WebDriverManager):
        self.webdriver_manager = webdriver_manager

    def configure(self, binder):
        
        driver = self.webdriver_manager.get_driver()
        binder.bind(webdriver.Chrome, to=driver, scope=singleton)

