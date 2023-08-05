import asyncio
from injector import inject

from web_crawler_app.crawl_pages.benefits_by_cpf_search_page import BenefitsByCPFSearchPage
from web_crawler_app.crawl_pages.login_page import LoginPage

class WebScrapperApp:
    @inject
    def __init__(self, login_page: LoginPage, benefits_by_cpf_page: BenefitsByCPFSearchPage):
        self.login_page = login_page
        self.benefits_by_cpf_page = benefits_by_cpf_page
        self.results = None
    
    async def make_manager_benefits_module(self, username, password, cpf):
        task_login = self.login_page.perfom_login_async(username, password)
        
        task_click_menu = self.benefits_by_cpf_page.click_benefits_by_cpf_menu()

        task_click_search_cpf = self.benefits_by_cpf_page.search_by_cpf(cpf)

        
        await asyncio.gather(task_login, task_click_menu, task_click_search_cpf)


    async def run(self, username, password, cpf):
        try:
            await asyncio.gather(self.make_manager_benefits_module(username, password, cpf))
            event_loop = asyncio.get_running_loop()
            collect_results = await event_loop.create_task(self.benefits_by_cpf_page.collect_results())

            return collect_results
        except Exception as e:
            return e