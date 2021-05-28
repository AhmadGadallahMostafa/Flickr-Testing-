from selenium.webdriver.common.by import By

class LogoutPageLocators(object):
    ACCOUNT = (By.XPATH, "//div[contains(@class,'avatar person tiny')]")
    LOGOUT = (By.LINK_TEXT, "Log out")
    CHOOSE_AN_ACCOUNT = (By.XPATH, "//h6")
