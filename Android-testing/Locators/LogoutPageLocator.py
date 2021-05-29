from appium.webdriver.common.mobileby import MobileBy
class LogoutPageLocator:
    PROFILE = (MobileBy.ACCESSIBILITY_ID, "Profile")
    SETTINGS = (MobileBy.ID, "com.flickr.android:id/profile_header_overflow")
    SIGNOUT = (MobileBy.ID, "com.flickr.android:id/profile_settings_logout")
    GET_STARTED = (MobileBy.ACCESSIBILITY_ID, "Get Started")
