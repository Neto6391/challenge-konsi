import asyncio
from concurrent.futures import ThreadPoolExecutor
import aiohttp
from injector import inject, singleton
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@singleton
class BenefitsByCPFSearchPage:
    @inject
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    async def click_benefits_by_cpf_menu(self):
        benefits_by_cpf_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-button[contains(., 'Encontrar Benefícios de um CPF')]"))
        )
        print(benefits_by_cpf_menu)
        await self.click_element(benefits_by_cpf_menu)

    async def search_by_cpf(self, cpf):
        ion_item_with_cpf_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-input[@placeholder='Digite o número do CPF . . .']"))
        )
        await self.click_element(ion_item_with_cpf_input)

        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", ion_item_with_cpf_input, cpf)
        
        button_search = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, ".//ion-button[normalize-space() = 'Procurar']"))
        )
        await self.click_element(button_search)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-card[contains(@class, 'loading')]"))
        )

    async def execute_script_async(self, script, element):
        with ThreadPoolExecutor() as executor:
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(executor, self.driver.execute_script, script, element)

    async def click_element(self, element):
        await self.execute_script_async("arguments[0].click();", element)

    async def collect_results(self):
        benefits_found_card = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//ion-card[.//ion-card-header[contains(., 'BENEFÍCIOS ENCONTRADOS!')]]"))
        )

        ion_item = WebDriverWait(benefits_found_card, 5).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-item"))
        )
        

        ion_label = WebDriverWait(ion_item, 5).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-label"))
        )
        value_ion_label = ion_label.get_attribute("textContent")
        return value_ion_label
