import allure
from numpy.matlib import empty
from playwright.sync_api import expect
from pages.All_PagesObjectHandler import PageObjectHandler
from utils.logger import get_logger

logger = get_logger("Test End To End Workflow")

@allure.feature("End To End Test Workflow")
@allure.story("End To End Testing")

def test_endToend(browserInstance, testData, logger):

    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]
    expectedModules = testData["expected_modules"]


    logger.info("Starting End To End Test")


    # Step 1 : Login to Orange HRM
    poHandler = PageObjectHandler(browserInstance)
    loginPage = poHandler.getLoginPage()
    dashboardPage = poHandler.getDashboardPage()

    #loginPage = LoginPage(browserInstance)
    with allure.step("Step 1: Navigate to Login Page"):
        logger.info("Navigating to Login Page")
        loginPage.navigate(url)

    with allure.step("Step 2: Enter Credentials and Login"):
        try:
            logger.info(f"Enter Username: {username}")
            logger.info(f"Enter Password: {password}")
            loginPage.login(username,password)
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

    with allure.step("Step 4: Verify all components available after login page."):
        try:
            logger.info("Verifying all components After Login")
            menuItems, missing_modules = dashboardPage.verify_AllComponents(expectedModules)
            assert missing_modules == [] ,f"Unexpected modules found: {missing_modules}"
            logger.info(f"Menu List is : {menuItems}")
        except Exception as e:
            logger.error(f"Failed to get Tasks List {e}")
            raise

    with allure.step("Step 5: Verify tasks inside dashboard page"):
        try:
            taskList = dashboardPage.verifyTasks()
            logger.info(f"Today's Task List is : {taskList}")
        except Exception as e:
            logger.error(f"Failed to get Task List {e} ")
            raise e

    with allure.step("Step 6 : Verify User about details and get number of total employee"):
        try:
            logger.info("Click into User details")
            empCount = dashboardPage.verify_employeeCount()
            logger.info(f"Total Employee Count is {empCount}")
        except Exception as e:
            logger.error(f"Failed to get Employee count")

    with allure.step("Step 7: Verify Log Out"):
        try:
            logger.info("Click Log Out")
            dashboardPage.logOut()
            logger.info("User got logged out")
            logger.info("Test Passed - End To End Workflow.............")
        except Exception as e:
            logger.error(f"Failed to Logout")






























