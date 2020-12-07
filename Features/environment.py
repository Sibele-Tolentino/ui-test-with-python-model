from browser import Browser
from allure_behave.hooks import allure_report

allure_report("path/to/result/dir")

def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.browser_quit()

def after_scenario(context, scenario):
    context.browser.browser_clear()