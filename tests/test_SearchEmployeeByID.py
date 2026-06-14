from playwright.sync_api import expect
import allure,pytest
from pages.PageObjectHandler import PageObjectHandler
from utils.employeeRecords import Generate_CSV
from utils.logger import get_logger

logger = get_logger("Test Search Employee - PIM Module")

@allure.feature("PIM Module")
@allure.story("Search Employee")

@pytest.mark.order(2)
def test_SearchEmployee(browserInstance, testData, logger):
    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]
    emp_ID = testData["empId"]
    emp_Name = testData["employeeName"]["firstName"]

    logger.info("Starting Login Test")

    # Step 1 : Login to Orange HRM
    poHandler = PageObjectHandler(browserInstance)
    loginPage = poHandler.getLoginPage()
    dashboardPage = poHandler.getDashboardPage()
    PIMpage = poHandler.getPIMModule()
    genCSV = Generate_CSV(browserInstance)

    # loginPage = LoginPage(browserInstance)
    with allure.step("Step 1: Navigate to Login Page"):
        logger.info("Navigating to Login Page")
        loginPage.navigate(url)

    with allure.step("Step 2: Enter Credentials and Login"):
        try:
            logger.info(f"Enter Username: {username}")
            logger.info(f"Enter Password: {password}")
            loginPage.login(username, password)
            logger.info(f"Login Successful")
        except Exception as e:
            logger.error(f"Failed to Login : {e}")
            raise

    with allure.step("Step 3: Verify User landed on Dashboard Page"):
        try:
            logger.info("Validating dashboard")
            expect(dashboardPage.verifyDashboardPage()).to_be_visible()
            logger.info("Dashboard page is visible")
        except Exception as e:
            logger.error(f"Not Landed on Dashboard page : {e}")
            raise

    with allure.step("Step 4: Go To PIM Module"):
        try:
            logger.info("Go To PIM Module")
            PIMpage.clickPIMModule()
            logger.info("Inside PIM Module")
        except Exception as e:
            logger.error(f"Not able to go inside PIM {e}")
            raise

    with allure.step("Step 5:Search for an employee by ID"):
        try:
            # Generate CSV first
            csv_path = genCSV.generate_employee_csv()

            print(csv_path)
            logger.info(f"CSV Path = {csv_path}")
            logger.info(f"Searching for employee with ID {emp_ID}")
            record = PIMpage.searchEmployeeByID(emp_ID,csv_path)
            logger.info(f"{record}")
            assert "(1)" in record

        except Exception as e:
            logger.error(f"Search Got failed {e}")
            raise




















