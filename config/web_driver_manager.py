from selenium import webdriver
from injector import Module, singleton
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriverManager:
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self.initialize_driver()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_driver()
        return False 

    def initialize_driver(self):
        if not self.driver:
            driver_path = ChromeDriverManager().install()
            options = Options()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=options)
            

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_driver(self):
        return self.driver