from playwright.sync_api import Page, expect

class ActionsPage:

    def __init__(self, page:Page):
        self.page = page

    def get_by_placeholder(self,locator):
        self.page.get_by_placeholder(locator)

    def get_by_role(self,locator):
        self.page.get_by_role(locator)

    def get_by_text(self,locator):
        self.page.get_by_text(locator)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()