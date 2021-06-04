from selenium.webdriver.common.by import By
class ExplorePageLocators(object):
    PHOTOS = (By.CLASS_NAME, "photo-list-photo-interaction")
    TRENDING_TAB = (By.ID, "tags")
    TRENDING_TAG_TITLES = (By.CLASS_NAME, "tag-list-header")
    TRENDING_PHOTOS = (By.XPATH, "//div[@class='view photo-list-view']")