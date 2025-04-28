Feature: Python Search
    Scenario: Busqueda de Python en Wikipedia
    Given el usuario se encuentra en la pagina de Wikipedia
    When el usuario escribe Python (lenguaje de programación) en la barra de busqueda
    Then aparece un articulo relacionado a Python