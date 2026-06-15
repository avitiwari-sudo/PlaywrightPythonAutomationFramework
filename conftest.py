import pytest,json,allure
from pathlib import Path

from playwright.sync_api import Playwright
from pages.All_PagesObjectHandler import PageObjectHandler
from utils.logger import get_logger

@pytest.fixture(scope="session")
def user_credentials(request):  # request is used to access both global variable env and local variables
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chromium or firefox"
    )

@pytest.fixture
def testData():
    root = Path.cwd()  # pytest rootdir in CI
    file_path = root / "data" / "testcase_variable_resource.json"
    return json.loads(file_path.read_text())


@pytest.fixture
def logger(request):
    test_name = request.node.name
    return get_logger(test_name)

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)

    context = browser.new_context()
    page = context.new_page()
    yield page

    context.close()
    browser.close()

# API Login using cookies
@pytest.fixture
def authenticated_api_context(playwright):

    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/dashboard/**")

    cookies = page.context.cookies()

    cookie_value = next(
        c["value"]
        for c in cookies
        if "orangehrm" in c["name"].lower()
    )

    api_context = playwright.request.new_context(
        base_url="https://opensource-demo.orangehrmlive.com",
        extra_http_headers={
            "Cookie": f"orangehrm={cookie_value}"
        }
    )

    yield api_context

    api_context.dispose()
    browser.close()

@pytest.fixture
def api_context(browserInstance,playwright:Playwright,testData):
    url = testData["url"]
    username = testData["user_credentials"]["username"]
    password = testData["user_credentials"]["password"]
    poHandler = PageObjectHandler(browserInstance)
    loginpage = poHandler.loginPage
    loginpage.navigate(url)
    loginpage.login(username, password)

    browserInstance.wait_for_url("**/dashboard/**")

    cookies = browserInstance.context.cookies()

    cookie_header = "; ".join(
        [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
    )

    api_context = playwright.request.new_context(
        base_url="https://opensource-demo.orangehrmlive.com",
        extra_http_headers={
            "Cookie": cookie_header
        }
    )
    yield api_context

    api_context.dispose()









@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Only take screenshot on test failure
    if result.when == "call" and result.failed:
        page = item.funcargs.get("browserInstance")
        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


