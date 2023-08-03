from selenium import webdriver
from injector import Module
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class WebDriverConfig(Module):
    def __init__(self, headless: bool = True):
        self.headless = headless

    def configure(self, binder):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
            print("True headless?")
        
        driver_path = ChromeDriverManager().install()
        binder.bind(webdriver.Chrome, to=webdriver.Chrome(service=Service(executable_path=driver_path), options=options))

