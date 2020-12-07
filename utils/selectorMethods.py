from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from browser import Browser

class ElementFinder(Browser):
    def find_element(self, selector, method):
        if method == 'CSS_SELECTOR':
            clickable_element = self.driver.find_element_by_css_selector(selector)
            print('CSS\n')
            try:
                element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            finally:
                print('NOT FOUND\n')
        elif method == 'CLASS_NAME':
            print('CLASS\n')
            clickable_element = self.driver.find_element_by_class_name(selector)
            try:
                element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, selector)))
            finally:
                print('NOT FOUND\n')
        elif method == 'XPATH':
            print('XPATH\n')
            clickable_element = self.driver.find_element_by_xpath(selector)
            try:
                element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, selector)))
            finally:
                print('NOT FOUND\n')
        elif method == 'ID':
            print('ID\n')
            clickable_element = self.driver.find_element_by_id(selector)
            try:
                element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, selector)))
            finally:
                print('NOT FOUND\n')
        else:
            print('NOT CATALOGED\n')

        return clickable_element


