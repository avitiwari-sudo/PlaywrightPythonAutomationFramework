import csv

import pandas as pd
from playwright.sync_api  import Playwright,Page


class Generate_CSV:
    def __init__(self,page:Page):
        self.page = page
        
    def generate_employee_csv(self):
        data = []
        csv_path = "updated_orangehrm_employees.csv"

        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        self.page.wait_for_load_state("networkidle")
    
        # Get all page number buttons
        page_numbers = self.page.locator(".oxd-pagination-page-item:not(.oxd-pagination-page-item--previous-next)")
    
        total_pages = page_numbers.count()
    
        print(f"Total pages Found: {total_pages}")
    
        for page_index in range(total_pages):
    
            print(f"\nProcessing page {page_index+1}")
    
            self.page.locator(".oxd-table-body").wait_for()
    
            rows = self.page.locator(".oxd-table-body .oxd-table-card")
    
            row_count = rows.count()
    
            print(f"Rows Found: {row_count}")
    
            for row_index in range(row_count):
                row = rows.nth(row_index)
    
                columns = row.locator(".oxd-table-cell").all_inner_texts()
    
                cleaned_columns = [col.strip() for col in columns]
    
                data.append(cleaned_columns)
    
            # Move to next page
            if page_index < total_pages - 1:
                page_numbers = self.page.locator(".oxd-pagination-page-item:not(.oxd-pagination-page-item--previous-next)")
                page_numbers.nth(page_index + 1).click()
    
                self.page.wait_for_load_state("networkidle")
                self.page.wait_for_timeout(2000)

        # Update CSV

        df = pd.DataFrame(
            data,
            columns=[
                "Checkbox",
                "Employee_Id",
                "First_Name",
                "Last_Name",
                "Job_Title",
                "Employment_Status",
                "Sub_Unit",
                "Supervisor",
                "Actions"
            ]
        )

        df = df.drop(["Checkbox","Actions"], axis=1)

        df.to_csv(csv_path, index=False)

        return csv_path


    def totalRecords(self,csv_path):

        df = pd.read_csv(csv_path)

        return len(df)
        newData.to_csv(csv_path, index=False)


        print(f"CSV generated: {csv_path}")
        print(f"Total rows: {len(df)}")

        return csv_path


    # def totalRecords(self,csv_path):
    #     with open(csv_path, "r") as file:
    #         reader = csv.reader(file)
    #         next(reader)  # It will not include header
    #         #total_records = sum(1 for row in reader)
    #         total_records = 0
    #         for row in reader:
    #             total_records += 1
    #         return total_records





