import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('godel escher bach')
search_box.send_keys('\uE007')