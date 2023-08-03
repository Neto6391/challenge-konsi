from injector import inject
from concurrent.futures import ThreadPoolExecutor

from web_crawler_app.crawl_pages.benefits_by_cpf_search_page import BenefitsByCPFSearchPage
from web_crawler_app.crawl_pages.login_page import LoginPage


class WebScrapperApp:
    @inject
    def __init__(self, login_page: LoginPage, benefits_by_cpf_page: BenefitsByCPFSearchPage, url: str):
        self.login_page = login_page
        self.benefits_by_cpf_page = benefits_by_cpf_page
        self.url = url
        self.results = None


    async def run(self, username, password, cpf):
        print("antes o primeiro await")
        # Executar o login de forma assíncrona
        await self.login_page.perfom_login_async(username, password)
        print("apos o primeiro await")

        # Clicar no menu de "benefícios por CPF"
        await self.benefits_by_cpf_page.click_benefits_by_cpf_menu()
        print("apos o segundo await")

        await self.benefits_by_cpf_page.search_by_cpf(cpf)

        self.results = await self.benefits_by_cpf_page.collect_results()

        return self.results
