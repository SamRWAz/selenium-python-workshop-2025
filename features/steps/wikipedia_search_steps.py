from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_search_page import WikipediaSearch

@given('el usuario se encuentra en la pagina de Wikipedia')
def step_given_wikipedia_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.wikipedia_search_page= WikipediaSearch(context.driver)

@when('el usuario escribe Python (lenguaje de programación) en la barra de busqueda')
def step_when_wikipedia_search(context):
    context.wikipedia_search_page.searchConcept("Python (lenguaje de programación)")

@then('aparece un articulo relacionado a Python')
def step_then_searched_concept(context):
    assert "Python" in context.wikipedia_search_page.isElementPresent()