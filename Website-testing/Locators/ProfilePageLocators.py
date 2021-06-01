from selenium.webdriver.common.by import By
class ProfilePageLocators(object):
    FOLLOW_BUTTON = (By.XPATH, "//button[@class='follow white']")
    FOLLOW_TEXT = (By.XPATH, "//div[@class='view follow-view']")