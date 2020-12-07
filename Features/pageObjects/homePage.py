from selenium.webdriver.support import expected_conditions as EC
from Features.elements.homeElementsPage import PageLocatorHome
from selenium.webdriver.support.ui import WebDriverWait
from utils.selectorMethods import ElementFinder
from selenium import webdriver
from browser import Browser

PageLocatorHome = PageLocatorHome()
ElementFinder = ElementFinder()

class HomePage(Browser):

    def access_login_page(self):
        element = ElementFinder.find_element(PageLocatorHome.entrar_button, 'CSS_SELECTOR')
        element.click()

    def access_books_page(self):
        element = ElementFinder.find_element(PageLocatorHome.books_button, 'CSS_SELECTOR')
        element.click()
