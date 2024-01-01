import requests
from unittest import TestCase
from selenium import webdriver

from base.locators import Links
from pages.login_page import LoginPage

class TestIssac(TestCase):
    def setUp(self) -> None:
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get(Links.MAIN_LINK)
        self.test_login = LoginPage(self.driver)
    
    def test1_login_empty(self):
        username = ""
        password = ""
        self.test_login.log_in(username, password)
        self.test_login.check_error()
        
        
    def test2_login_wrong(self):
        username = "asdasdlkjsahk"
        password = "456461231231"
        self.test_login.log_in(username, password) 
        self.test_login.check_error()
        
        
    def test3_login_right(self):
        initial_url = self.driver.current_url
        username = "standard_user"
        password = "secret_sauce"
        self.test_login.log_in(username, password)
        if(initial_url == self.driver.current_url):
            assert False
        
    def tearDown(self) -> None:
        self.driver.quit()