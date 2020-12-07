from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Features.pageObjects.booksPage import BooksPage
from selenium import webdriver
from browser import Browser
from nose.tools import *
from behave import *

BooksPage = BooksPage()

@then(u'I see books page')
def step_impl(context):
    assert_equal(BooksPage.get_text_book_page(),"Loja de Livros |\xa0Amazon.com.br")