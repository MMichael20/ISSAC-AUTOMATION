from base.base_page import BasePage
from base.locators import LoginLocators as l
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        
    def log_in(self, username, password):
        self.enter_text(*l.USERNAME_INPUT, username) 
        self.enter_text(*l.PASSWORD_INPUT, password)
        self.click_element(*l.SUBMIT_BUTTON)
        
    def check_error(self):
        try:
            self.click_element(*l.ERROR_MESSAGE)
            assert True
        except NoSuchElementException:
            assert False
        
    
        