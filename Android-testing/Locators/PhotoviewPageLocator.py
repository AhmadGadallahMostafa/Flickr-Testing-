from appium.webdriver.common.mobileby import MobileBy

class PhotoviewPageLocator:
    TITLE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_title_left")
    CLOSE_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_up")
