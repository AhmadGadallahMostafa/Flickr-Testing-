from selenium.webdriver.common.by import By
class PhotoStreamLocators(object):
    TITLE = (By.CLASS_NAME, "interaction-bar")
    PHOTO = (By.XPATH,"//div[@class='view photo-list-photo-view photostream awake']")


