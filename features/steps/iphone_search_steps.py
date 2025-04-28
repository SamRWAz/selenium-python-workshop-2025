from behave import given, when, then
from selenium import webdriver
from pages.iphone_search_page import IphoneSearch

@given('el usuario se encuentra en la pagina de Mercado Libre')
def step_given_iphone_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.iphone_search_page= IphoneSearch(context.driver)

@when('el usuario escribe iPhone 13 en la barra de busqueda')
def step_when_intu_login(context):
    context.iphone_search_page.searchIphone("iPhone 13")

@then('aparece un listado de productos asociados a la palabra iPhone 13')
def step_then_iphone_catalog(context):
    assert "Iphone 13" in context.iphone_search_page.isElementPresent()