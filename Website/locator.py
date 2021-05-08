from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.LINK_TEXT, "Log In")


class LoginPageLocators(object):
    NEXT_BUTTON = (By.CSS_SELECTOR, "button")


class HomePageLocators(object):
    UPLOAD_ICON = (By.CLASS_NAME, "upload-icon")
    YOU = (By.XPATH, "//ul[@class='nav-menu desktop-only']//li[1]")
    GROUPS_ICON = (By.XPATH, "//ul[@class='gn-submenu']//li[6]")
    NOTIFICATIONS_ICON = (By.XPATH, "//ul[@class='gn-tools']/li[3]")
    PUSH_NOTIFICATION = (By.XPATH, "//div[@class='view notifications-menu-view']/a/span/span")
    SEARCH_PEOPLE = (By.PARTIAL_LINK_TEXT, "People")
    SEARCH_FIELD = (By.ID, "search-field")
    NOTIFICATION = (By.XPATH, "//ul[@class='notifications-list']//li[2]")

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


class GroupsPageLocators(object):
    CREATE_GROUP = (By.PARTIAL_LINK_TEXT, "Create Group")
    NEXT = (By.XPATH, "//button[@class='mini action button-action']")
    ERROR_TEXT = (By.XPATH, "//div[@class='error-message title-error']")
    GROUP_NAME_TEXT = (By.XPATH, "//input[@class='input-field group-name']")
    AGE_18_TEXT = (By.PARTIAL_LINK_TEXT, "This group is 18+")
    ADULT_GROUP_SELECTOR = (By.XPATH, "//label[@for='adult-group']/div")
    GROUP_MESSAGE = (By.XPATH, "//div[@role='main']")
    PHOTO_POOL = (By.ID, "pool")
    GROUP_LINK = (By.XPATH, "//div[@class='view sortable-table-view']/div/table/tbody/tr[2]/td[1]/a")
    ADD_PHOTO = (By.PARTIAL_LINK_TEXT, "Add photo")
    PHOTO_BOX = (By.XPATH, "//div[@id='pp-source']/ul/li[1]")
    PHOTO_BOX_SELECTED = (By.XPATH, "//div[@id='pp-source']/ul/li[1]")
    ADD_TO_GROUP = (By.ID, "pp-add-photos")
    PHOTO_UPLOADED_TITLE = (By.CLASS_NAME, "interaction-bar")

class SearchPeoplePageLocators(object):
    FOLLOW_BUTTON = (By.XPATH, "//button[@class='follow ']")