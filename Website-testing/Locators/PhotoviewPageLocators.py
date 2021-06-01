from selenium.webdriver.common.by import By
class PhotoViewLocators(object):
    COMMENT_TEXTBOX = (By.NAME, "comment")
    COMMENT_BUTTON = (By.LINK_TEXT,"Comment")
    COMMENT_TEXT = (By.XPATH, "//div[@class='comment-content']")