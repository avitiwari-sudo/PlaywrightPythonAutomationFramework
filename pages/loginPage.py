from playwright.sync_api import expect,Page
from pages.locators.locators import Locators


class LoginPage():
    def __init__(self,page:Page):
        self.page = page

    def navigate(self,url):
        #self.logger.info("Navigating to Login Page")
        self.page.goto(url)

    def login(self,username, password):
            self.page.get_by_placeholder(Locators.USERNAME_INPUT).fill(username)
            self.page.get_by_placeholder(Locators.PASSWORD_INPUT).fill(password)
            self.page.locator(Locators.LOGIN_BUTTON).click()



















