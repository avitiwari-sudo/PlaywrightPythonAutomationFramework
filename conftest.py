import pytest,json,allure
from pathlib import Path
from playwright.sync_api import Playwright

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


