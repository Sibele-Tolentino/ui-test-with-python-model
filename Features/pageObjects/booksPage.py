from selenium.webdriver.support import expected_conditions as EC
from Features.elements.booksElementsPage import PageLocatorBooks
from selenium.webdriver.support.ui import WebDriverWait
from utils.selectorMethods import ElementFinder
from selenium import webdriver
from browser import Browser

ElementFinder = ElementFinder()
PageLocatorBooks = PageLocatorBooks()

class BooksPage(Browser):

    def get_text_book_page(self):
        current_url = self.driver.current_url
        self.driver.get(current_url)
        print(self.driver.title)
        return self.driver.title
