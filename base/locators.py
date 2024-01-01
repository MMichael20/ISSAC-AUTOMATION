from selenium.webdriver.common.by import By

class Links(object):
    MAIN_LINK = "https://www.saucedemo.com/"

class LoginLocators(object):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")