import pytest,allure
from api.employeeAPI import EmployeeAPI
from utils.employeeRecords import Generate_CSV

@pytest.mark.order(3)
def test_getEmployeeTotalCount(browserInstance,api_context,testData,logger):

    employeeList = EmployeeAPI(api_context)
    emp_ID = testData["empId"]
    emp_name = testData["employeeName"]["firstName"]
    genCSV = Generate_CSV(browserInstance)

    with allure.step("Step-1: Fetching Employee Details"):
        try:
            all_employees_response = employeeList.getEmployees()
            json_data_employees = all_employees_response.json()
            totalEmployeesAPI = int(json_data_employees['meta']['total'])
            csv_path = genCSV.generate_employee_csv()
            totalEmployeesUI = genCSV.totalRecords(csv_path="updated_orangehrm_employees.csv")
            assert totalEmployeesAPI == totalEmployeesUI, "Total Employees are not matching"
            logger.info(f"EmployeeAPI = {totalEmployeesAPI} matching with EmployeeUI= {totalEmployeesUI}")
        except Exception as e:
            raise e

