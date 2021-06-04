from appium.webdriver.common.mobileby import MobileBy
class ProfilePageLocator(object):
    FOLLOW_BTN = (MobileBy.ID, "com.flickr.android:id/follow_btn_icon")
    FOLLOW_STATUS = (MobileBy.ID, "com.flickr.android:id/follow_btn_text")