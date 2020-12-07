from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from browser import Browser
import time

class PageLocatorLogin(object):
        login_user_email = '#ap_email'
        login_home = '#ng-app > main > header > div > svg'
        login_user_password = '#password'
        login_sign_button = '#continue'
        login_error_message = '#auth-error-message-box > div > h4'