import allure
import pytest

from pages.loginPage import LoginPage

@allure.feature("Login Module")
@allure.story("Valid Login")

def test_Login(browserInstance, testData):

    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]


    # Step 1 : Login to Orange HRM
    loginPage = LoginPage(browserInstance)
    with allure.step("Step 1: Navigate to Login Page"):
        loginPage.navigate(url)

    with allure.step("Step 2: Enter Credentials and Login"):
        loginPage.login(username,password)













