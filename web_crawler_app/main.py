from injector import Injector
from config.web_driver_config import WebDriverConfig

from web_crawler_app.app.web_scrapper import WebScrapperApp


def crawl_benefit_cpf(username: str, password: str, cpf: str):
    try:
        injector = Injector([WebDriverConfig(headless=True)])
        app = injector.get(WebScrapperApp)
        benefit = app.run(username, password, cpf)
        print("Benefit: ", benefit)
    except Exception as e:
        print(f"Something was happening: {e}")
