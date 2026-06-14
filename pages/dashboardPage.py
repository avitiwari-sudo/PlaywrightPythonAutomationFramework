from playwright.sync_api import Page,expect
from pages.locators.locators import Locators
from utils.logger import get_logger

class DashboardPage:
    def __init__(self,page:Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def verifyDashboardPage(self):
        self.page.wait_for_load_state("networkidle")
        return self.page.locator(Locators.DASHBOARD)

    def verify_AllComponents(self, expected_modules):

        # Tested by tweaking expected results , now menuItems is having more module than expected - Dev mistake they did not tell us

        menuItems = self.page.locator(Locators.MENU_LIST).all_text_contents()

        unmatched_modules = [
            module for module in menuItems
            if module not in expected_modules
        ]
        return menuItems , unmatched_modules


    def verify_AllComponents_is_clickable(self,expected_modules):
        menuItems,_ = self.verify_AllComponents(expected_modules)
        clickedItems = []
        for item in menuItems:
            self.page.locator(Locators.SEARCH_MENU).fill(item)
            if item == "Maintenance":
                continue
            self.page.get_by_role("link", name=f"{item}").click()
            # if item == "Maintenance":
            #     self.page.get_by_role("link", name=f"{item}").click()
            #     self.page.locator("input[type='password']").fill(password)
            #     self.page.get_by_text(" Confirm ").click()
            expect(self.page.locator(Locators.MENU_HEADERS)).to_be_visible()
            clickedItems.append(item)
        return clickedItems

    def verifyTasks(self):
        tasksDetails = self.page.locator(Locators.TASKS_LIST).all_text_contents()
        return tasksDetails

    def verify_employeeCount(self):
        self.page.locator(Locators.USERNAME).click()
        self.page.get_by_text(Locators.ABOUT).click()
        self.page.locator(Locators.MODEL).wait_for()
        active_emp_count = self.page.locator(Locators.EMPLOYEE_COUNT).nth(2).inner_text()
        self.page.locator(Locators.CLOSE_BUTTON).click()
        return active_emp_count

    def logOut(self):
        self.page.locator(Locators.USERNAME).click()
        self.page.get_by_text(Locators.LOGOUT).click()
        expect(self.page.locator(Locators.LOGIN_TITLE)).to_be_visible()







