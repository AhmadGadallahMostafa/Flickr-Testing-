from selenium.webdriver.common.by import By

class MainPageLocators(object):

    LOGIN_BUTTON = (By.LINK_TEXT, "Log In")


class LoginPageLocators(object):

    NEXT_BUTTON = (By.CSS_SELECTOR, "button")
    EMAIL_TEXTBOX = (By.ID,"login-email")
    LOGIN_BUTTON = (By.XPATH,"//button")
    EMAIL_WARNING = (By.XPATH, "//div[contains(@class,'flickr-modal bg-white elevation-2 b-rad-1 flex column pa-3')]")
    EMAIL_REQUIRED = (By.XPATH, "//form[@id='login-form']//div[2]//div[2]")
    PASSWORD_TEXTBOX = (By.ID, "login-password")
    PASSWORD_REQUIRED = (By.XPATH, "//form[@id='login-form']//div[3]//div[1]//div[2]")
    INVALID_EMAIL_OR_PASSWORD = (By.XPATH, "//p")
class HomePageLocators(object):

    UPLOAD_ICON = (By.CLASS_NAME, "upload-icon")
    YOU = (By.XPATH, "//ul[@class='nav-menu desktop-only']//li[1]")


class UploadPageLocators(object):

    CHOOSE_PHOTO = (By.ID, "button-add-photos")
    DIALOG_BOX = (By.ID, "editr-publish-dialog")
    PUBLISH = (By.ID, "action-publish")
    CONFRIM_PUBLISH = (By.ID, "confirm-publish")
    USER_MESSAGING = (By.ID, "user-messaging")
    REMOVE_FILE_BUTTON = (By.ID, "action-remove-errors")
    PHOTOSTREAM_LINK = (By.CLASS_NAME, "gn-link")
    UPLOAD_BOX = (By.CLASS_NAME, "selected-wrapper")


class PhotoStreamLocators(object):

    TITLE = (By.CLASS_NAME, "interaction-bar")


class SearchResultsPageLocators(object):
    pass


class LogoutLocators(object):
    ACCOUNT = (By.XPATH, "//div[contains(@class,'avatar person tiny')]")
    LOGOUT = (By.LINK_TEXT, "Log out")
    CHOOSE_AN_ACCOUNT = (By.XPATH, "//h6")

class SignupPageLocators(object):
    FIRST_NAME = (By.ID, "sign-up-first-name")
    LAST_NAME = (By.ID, "sign-up-last-name")
    AGE = (By.ID, "sign-up-age")
    EMAIL = (By.ID, "sign-up-email")
    PASSWORD = (By.ID, "sign-up-password")
    SIGNUP = (By.XPATH, "//button")
    FIRST_NAME_REQUIRED = (By.XPATH, "//form[@id='sign-up-form']//div[1]//div[2]")
    LAST_NAME_REQUIRED = (By.XPATH, "//form[@id='sign-up-form']//div[2]//div[2]")
    AGE_REQUIRED = (By.XPATH, "//form[@id='sign-up-form']//div[3]//div[2]")
    EMAIL_REQUIRED = (By.XPATH, "//form[@id='sign-up-form']//div[4]//div[2]")
    PASSWORD_REQUIRED = (By.XPATH, "//form[@id='sign-up-form']//div[5]//div[2]")
    AGE_WARNING = (By.XPATH, "//form[@id='sign-up-form']//div[3]//div[2]")
    EMAIL_WARNING = (By.XPATH, "//form[@id='sign-up-form']//div[4]//div[2]")
    PASSWORD_WARNING = (By.XPATH, "//form[@id='sign-up-form']//div[5]//div[2]")



