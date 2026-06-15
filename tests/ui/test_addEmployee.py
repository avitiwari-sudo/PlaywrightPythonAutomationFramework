from playwright.sync_api import expect
import allure,pytest
from utils.jsonUtils import update_testdata
from pages.All_PagesObjectHandler import PageObjectHandler
from utils.logger import get_logger

logger = get_logger("Test Add Employee - PIM Module")


@allure.feature("PIM Module")
@allure.story("Add Employee")

@pytest.mark.order(1)
def test_addEmployee(browserInstance, testData, logger):
    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]
    empName = testData["employeeName"]

    logger.info("Starting Login Test")

    # Step 1 : Login to Orange HRM
    poHandler = PageObjectHandler(browserInstance)
    loginPage = poHandler.getLoginPage()
    dashboardPage = poHandler.getDashboardPage()
    PIMpage = poHandler.getPIMModule()

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

    with allure.step("Step 5:Add an employee and get an employee ID."):
        try:
            logger.info("Add an Employee")
            empId, success_msg = PIMpage.addEmployeeAndGetID(empName["firstName"],empName["middleName"],empName["lastName"])
            logger.info(
                f"Employee Details for {empName['firstName']} {empName['lastName']} got created with ID {empId}"
            )
            assert "Success" in success_msg
            # Store empId into existing data file

            update_testdata("data/testcase_variable_resource.json", "empId", empId)

        except Exception as e:
            logger.error(f"Could Not able to add Employee details {e}")
            raise









