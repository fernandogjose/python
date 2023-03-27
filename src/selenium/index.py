from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Firefox()

navegador.get("http://www.python.org")
assert "Python" in navegador.title

element = navegador.find_element(By.XPATH, '//*[@id="id-search-field"]')
element.send_keys('pycon')
element.send_keys(Keys.RETURN)
assert "No results found." not in navegador.page_source

navegador.close()

print('sucesso')