import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def set_download_folder(path):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {"profile.default_content_settings.popups": 0,
                "download.default_directory": path,
                "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    return options
def select_title(driver,title):
    if len(title) == 1:
        return None
    try:
        print(title)
        book_link = driver.find_element_by_partial_link_text(title)
        return book_link
    except:
        home_link = driver.find_element_by_id('logoText')
        home_link.click()
        search_box = driver.find_element_by_id('searchFieldx')
        title = title[0: len(title) - 1]
        search_box.send_keys(title)
        search_box.send_keys('\uE007')
        select_title(driver, title)

def download_book(title):
    options = set_download_folder("C:\\Users\\DELL\\Downloads\\ebook_downloads")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get('https://www.b-ok.xyz')
    signin_link = driver.find_element_by_class_name('dropdown-toggle')
    signin_link.click()
    dropdown_menu = driver.find_element_by_class_name('dropdown-menu')
    login_button = driver.find_element_by_link_text('Login')
    login_button.click()
    username_box = driver.find_element_by_id('username')
    username_box.send_keys('ammodaastronomar@gmail.com')
    password_box = driver.find_element_by_id('password')
    password_box.send_keys('rigelturk')
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    sleep(3)
    search_box = driver.find_element_by_id('searchFieldx')
    title_words = title.strip().split(' ')
    capitalized_title = title_words[0].capitalize().strip()
    for i in range(1,len(title_words)):
        capitalized_title += ' ' + title_words[i].capitalize().strip()
    title = capitalized_title
    search_box.send_keys(title)
    search_box.send_keys('\uE007')
    book_link = driver.find_element_by_partial_link_text(title)
    # if book_link is None:
    #     print('No match for book')
    #     return
    book_link.click()
    download_button = driver.find_element_by_class_name('dlButton')
    download_button.click()
    sleep(10)

if __name__ == '__main__':
    download_book("Harry Potter")





