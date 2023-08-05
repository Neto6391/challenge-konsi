from injector import Injector
from config.web_driver_config import WebDriverConfig
from config.web_driver_manager import WebDriverManager

from web_crawler_app.app.web_scrapper import WebScrapperApp
from selenium.common.exceptions import WebDriverException


async def crawl_benefit_cpf(username: str, password: str, cpf: str):
    try:
        webdriver_manager = WebDriverManager()
        with webdriver_manager as driver:
            injector = Injector([WebDriverConfig(webdriver_manager=webdriver_manager)])
            app = injector.get(WebScrapperApp)
            benefit = await app.run(username, password, cpf)
            if benefit != "Matrícula não encontrada!":
                return benefit
            else:
                return None
    except WebDriverException:
        return None
    except Exception as e:
        return None
