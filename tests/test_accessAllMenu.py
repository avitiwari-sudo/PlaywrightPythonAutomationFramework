import allure
from playwright.sync_api import expect
from pages.PageObjectHandler import PageObjectHandler
from utils.logger import get_logger

logger = get_logger("Access All Modules")



def test_AllModules(browserInstance, testData, logger):

    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]
    expectedModules = testData["expected_modules"]

    logger.info("Starting Login Test")


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

    with allure.step("Step 4: Click all menu and verify nothing is breaking"):
        try:
            logger.info("Accessing Modules")
            clickedItems = dashboardPage.verify_AllComponents_is_clickable(expectedModules)
            logger.info(f"Able to access all modules : {clickedItems}")
        except Exception as e:
            logger.error(f": failed to get Tasks List {e}")
            raise

    with allure.step("Step 5: Verify Log Out"):
        try:
            logger.info("Click Log Out")
            dashboardPage.logOut()
            logger.info("User got logged out")
            logger.info("Test Passed - All Modules were accessible")
        except Exception as e:
            logger.error(f"Failed to Logout : {e}")
