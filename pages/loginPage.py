import time
from time import sleep

from playwright.sync_api import expect,Page
from pages.locators.locators import Locators
from utils.logger import get_logger

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.logger = get_logger("LoginPage")


    def navigate(self,url):
        self.logger.info("Navigating to Login Page")
        self.page.goto(url)


    def login(self,username, password):
        try:
            self.logger.info(f"Entering Username: {username}")
            self.page.get_by_placeholder(Locators.USERNAME_INPUT).fill(username)

            self.logger.info(f"Entering Password: {password}")
            self.page.get_by_placeholder(Locators.PASSWORD_INPUT).fill(password)

            self.logger.info("Clicking Login Button")
            self.page.locator(Locators.LOGIN_BUTTON).click()
            self.logger.info("Login Successful")

            self.page.wait_for_load_state("networkidle")
            expect(self.page.locator(Locators.DASHBOARD)).to_be_visible()
            self.logger.info("Landed on DashBoard Page")

        except Exception as e:
            self.logger.error(f"Login Failed: {e}")
            raise















