from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class WikipediaSearch(BasePage):
    SEARCH_FIELD = (By.ID, 'searchInput')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/button')
    CONCEPT_SEARCHED = (By.XPATH, '/html/body/div[2]/div/div[3]/main/header/h1/span')

    def searchConcept(self, edit):
        self.enter_text(self.SEARCH_FIELD, edit)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.CONCEPT_SEARCHED)
        texto = elemento.text
        return texto
    
    