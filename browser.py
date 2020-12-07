from selenium import webdriver

class Browser(object):
    
    url_base = 'https://www.amazon.com.br/'
    
    driver = webdriver.Chrome()
    driver.get(url_base)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()
    
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

