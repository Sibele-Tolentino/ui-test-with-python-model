from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Features.pageObjects.loginPage import LoginPage
from selenium import webdriver
from browser import Browser
from nose.tools import *
from behave import *


from Features.elements.loginElementsPage import PageLocatorLogin
LoginPage = LoginPage()
PageLocatorLogin = PageLocatorLogin()

@when(u'I fill in the email')
def step_impl(context):
    LoginPage.send_user_email()

@when(u'I fill in the password')
def step_impl(context):
    LoginPage.send_user_password()

@when(u'I press sign button')
def step_impl(context):
    LoginPage.access_login_user()

@then(u'I see error login page')
def step_impl(context):
    assert_equal(LoginPage.get_text_login_page(), "Houve um problema")
