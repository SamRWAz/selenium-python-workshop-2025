from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class IphoneSearch(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.XPATH, '/html/body/header/div/div[2]/form/button/div')
    IPHONE_SEARCHED = (By.XPATH, '/html/body/main/div/div[2]/aside/div[1]/h1')

    def searchIphone(self, edit):
        self.enter_text(self.SEARCH_FIELD, edit)
        self.click(self.SEARCH_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.IPHONE_SEARCHED)
        texto = elemento.text
        return texto
    
    