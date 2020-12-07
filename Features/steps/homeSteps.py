from Features.pageObjects.homePage import HomePage
from browser import Browser

HomePage = HomePage()


@given(u'I acess base page')
def step_impl(context):
    print(f'\n\rAlready iniciate by browser')

@when(u'I press login')
def step_impl(context):
    HomePage.access_login_page()

@when(u'I press the books button')
def step_impl(context):
    HomePage.access_books_page()
