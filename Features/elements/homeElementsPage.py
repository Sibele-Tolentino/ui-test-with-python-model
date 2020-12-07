from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from browser import Browser
import time

class PageLocatorHome(object):
    entrar_button = '#nav-link-accountList > div > span'
    books_button = '#nav-xshop > a:nth-child(4)'