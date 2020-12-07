from selenium.webdriver.support import expected_conditions as EC
from Features.elements.loginElementsPage import PageLocatorLogin
from selenium.webdriver.support.ui import WebDriverWait
from utils.selectorMethods import ElementFinder
from selenium import webdriver
from browser import Browser
import json

ElementFinder = ElementFinder()
PageLocatorLogin = PageLocatorLogin()

with open('utils/data.json', 'r') as json_file:

    data = json.loads(json_file.read())
    invalid_email = data.get('invalid_login').get('email')
    invalid_password = data.get('invalid_login').get('password')

class LoginPage(Browser):

    def send_user_email(self):
        element = ElementFinder.find_element(
            PageLocatorLogin.login_user_email, 'CSS_SELECTOR')
        element.send_keys(invalid_email)

    def send_user_password(self):
        element = ElementFinder.find_element(
            PageLocatorLogin.login_user_password, 'CSS_SELECTOR')
        element.send_keys(invalid_password)

    def access_login_user(self):
        element = ElementFinder.find_element(
            PageLocatorLogin.login_sign_button, 'CSS_SELECTOR')
        element.click()

    def get_text_login_page(self):
        element = ElementFinder.find_element(PageLocatorLogin.login_error_message,'CSS_SELECTOR')
        return element.text
