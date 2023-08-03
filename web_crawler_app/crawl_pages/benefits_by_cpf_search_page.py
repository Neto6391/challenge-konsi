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

    def click_benefits_by_cpf_menu(self):
        benefits_by_cpf_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-button[contains(., 'Encontrar Benefícios de um CPF')]"))
        )
        self.click_element(benefits_by_cpf_menu)

    def search_by_cpf(self, cpf):
        ion_item_with_cpf_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-input[@placeholder='Digite o número do CPF . . .']"))
        )
        self.click_element(ion_item_with_cpf_input)

        self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", ion_item_with_cpf_input, cpf)
        
        button_search = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ".//ion-button[normalize-space() = 'Procurar']"))
        )
        self.click_element(button_search)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-card[contains(@class, 'loading')]"))
        )

    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def collect_results(self):
        benefits_found_card = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ion-card[.//ion-card-header[contains(., 'BENEFÍCIOS ENCONTRADOS!')]]"))
        )

        ion_item = WebDriverWait(benefits_found_card, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-item"))
        )
        

        ion_label = WebDriverWait(ion_item, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//ion-label"))
        )
        value_ion_label = ion_label.get_attribute("textContent")
        return value_ion_label
