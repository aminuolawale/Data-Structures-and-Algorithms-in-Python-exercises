import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.b-ok.xyz')
search_box = driver.find_element_by_id('searchFieldx')
print(search_box)
search_box.send_keys('Godel Escher Bach')