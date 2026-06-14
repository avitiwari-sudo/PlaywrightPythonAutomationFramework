class Locators:
    # Login Page Locators
    USERNAME_INPUT = "Username"
    PASSWORD_INPUT = "Password"
    LOGIN_BUTTON = "button[type='submit']"


    # Dashboard Page Locators
    DASHBOARD = "h6:has-text('Dashboard')"
    TASKS_LIST = ".orangehrm-todo-list-item .oxd-text"
    MENU_LIST = ".oxd-main-menu-item-wrapper .oxd-text"
    ABOUT = "About"
    USERNAME  = ".oxd-userdropdown-name"
    MODEL = ".oxd-dialog-container-default--inner"
    USER_ABOUT = ".oxd-userdropdown-link"
    EMPLOYEE_COUNT = "p[class*='oxd-text--p'][class$='-about-text']"
    CLOSE_BUTTON = "button[class$='-close-button-position']"
    SEARCH_MENU = "input[placeholder='Search']"
    MENU_HEADERS = "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"

    # Logout Locators
    LOGOUT = "Logout"
    LOGIN_TITLE = ".oxd-text.oxd-text--h5.orangehrm-login-title"

    # PIM page locators
    PIM = "span:has-text('PIM')"

    # ADD Employee
    ADD_EMPLOYEE = "Add Employee"
    FIRST_NAME = "First Name"
    MIDDLE_NAME = "Middle Name"
    LAST_NAME = "Last Name"
    DEFAULT_EMP_ID = "input[class$='--active']"
    ADD_EMP_SUCCESS = "div[class*='-toast--success']"
    SAVE_BUTTON ="Save"

    EMP_ID = "input[class='oxd-input oxd-input--active']"

    # Search Employee by ID related locators
    EMPLOYEE_LIST = "a:has-text('Employee List')"
    EMPLOYEE_ID = ".oxd-input.oxd-input--active:first-child"#".oxd-input--active"
    SEARCH = "Search"
    RECORD = ".orangehrm-horizontal-padding .oxd-text--span"

    # Pagination
    PAGINATION = ".oxd-pagination-page-item:not(.oxd-pagination-page-item--previous-next)"

    #In Progress
    # Search Employee By Name related locators

    RESET = "button[type='reset']"
    EMPLOYEE_TO_BE_SEARCH = "Type for hints..."






















