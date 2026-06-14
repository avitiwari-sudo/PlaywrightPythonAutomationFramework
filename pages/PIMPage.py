import csv
import time

import pandas as pd
from playwright.sync_api import expect,Page
from pages.locators.locators import Locators


class PIM:
    def __init__(self,page:Page):
        self.page = page
        data = []

    def clickPIMModule(self):
        self.page.locator(Locators.PIM).click()

    def addEmployeeAndGetID(self,firstName,middleName,lastName):
        # Click to add employee
        self.page.get_by_text(Locators.ADD_EMPLOYEE).click()

        # enter Employee details
        self.page.get_by_placeholder(Locators.FIRST_NAME).fill(firstName)
        self.page.get_by_placeholder(Locators.MIDDLE_NAME).fill(middleName)
        self.page.get_by_placeholder(Locators.LAST_NAME).fill(lastName)
        empId = self.page.locator(Locators.DEFAULT_EMP_ID).nth(1).input_value()
        self.page.get_by_text(Locators.SAVE_BUTTON).click()
        success_msg = self.page.locator(Locators.ADD_EMP_SUCCESS).text_content()
        return empId, success_msg

    def searchEmployeeByID(self, empID,csv_path):

        # Verify employee exists in CSV
        df = pd.read_csv(csv_path, dtype=str)
        employee = df[df["Employee_Id"] == str(empID)]
        if employee.empty:
            raise AssertionError(
                f"Employee ID {empID} not found in CSV"
            )
        print(
            f"Employee found in CSV: "
            f"{employee.iloc[0].to_dict()}"
        )

        self.page.locator(Locators.EMPLOYEE_LIST).click()
        expect(self.page.locator(Locators.EMPLOYEE_ID)).to_be_visible()
        self.page.locator(Locators.EMPLOYEE_ID).fill(empID)
        expect(self.page.get_by_text(Locators.SEARCH)).to_be_visible()
        self.page.get_by_text(Locators.SEARCH).click()
        self.page.wait_for_load_state("networkidle")

        #expect(self.page.locator(Locators.RECORD)).to_be_visible(timeout=5000)
        record = self.page.locator(Locators.RECORD).text_content()
        if "(1)" in record:
            return record
        return "No Records Found"






