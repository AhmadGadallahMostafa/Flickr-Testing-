from selenium.webdriver.common.by import By
class HomePageLocators(object):
    UPLOAD_ICON = (By.CLASS_NAME, "upload-icon")
    YOU = (By.XPATH, "//ul[@class='nav-menu desktop-only']//li[1]")
    GROUPS_ICON = (By.XPATH, "//ul[@class='gn-submenu']//li[6]")
    NOTIFICATIONS_ICON = (By.XPATH, "//ul[@class='gn-tools']/li[3]")
    PUSH_NOTIFICATION = (By.XPATH, "//div[@class='view notifications-menu-view']/a/span/span")
    SEARCH_PEOPLE = (By.PARTIAL_LINK_TEXT, "People")
    SEARCH_FIELD = (By.ID, "search-field")
    NOTIFICATION = (By.XPATH, "//ul[@class='notifications-list']//li[2]")
    PRINTS = (By.XPATH, "//ul[@class='nav-menu desktop-only']//li[3]/a")
