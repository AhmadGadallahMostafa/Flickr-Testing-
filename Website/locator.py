from selenium.webdriver.common.by import By


class MainPageLocators(object):

    LOGIN_BUTTON = (By.LINK_TEXT, "Log In")


class LoginPageLocators(object):

    NEXT_BUTTON = (By.CSS_SELECTOR, "button")


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
