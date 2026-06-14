from pages.dashboardPage import DashboardPage
from pages.loginPage import LoginPage
from pages.PIMPage import PIM

class PageObjectHandler:
    def __init__(self,page):
        self.page = page
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        self.PIMPage = PIM(page)

    def getLoginPage(self):
        return self.loginPage

    def getDashboardPage(self):
        return self.dashboardPage

    def getPIMModule(self):
        return self.PIMPage