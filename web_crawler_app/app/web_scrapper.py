from injector import inject
from concurrent.futures import ThreadPoolExecutor

from web_crawler_app.crawl_pages.benefits_by_cpf_search_page import BenefitsByCPFSearchPage
from web_crawler_app.crawl_pages.login_page import LoginPage


class WebScrapperApp:
    @inject
    def __init__(self, login_page: LoginPage, benefits_by_cpf_page: BenefitsByCPFSearchPage):
        self.login_page = login_page
        self.benefits_by_cpf_page = benefits_by_cpf_page
        self.results = None

    def run(self, username, password, cpf):
        with ThreadPoolExecutor() as executor:
            login_future = executor.submit(self.login_page.login, username, password) 
            
        login_future.result()
        
        self.benefits_by_cpf_page.click_benefits_by_cpf_menu()

        with ThreadPoolExecutor() as executor:
            search_future = executor.submit(self.benefits_by_cpf_page.search_by_cpf, cpf)
        
        search_future.result()

        with ThreadPoolExecutor() as executor:
            collect_results_future = executor.submit(self.benefits_by_cpf_page.collect_results)

        self.results = collect_results_future.result()

        return self.results