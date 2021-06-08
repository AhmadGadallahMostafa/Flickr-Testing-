from appium.webdriver.common.mobileby import MobileBy
class LoginPageLocators:
    EMAIL_FIELD = (MobileBy.ID, "com.example.mainhomefeed:id/et_email")
    PASSWORD = (MobileBy.ID, "com.example.mainhomefeed:id/et_passowrd")
    LOGIN_BTN = (MobileBy.ID, "com.example.mainhomefeed:id/btn_login")
    SIGNUP_BTN = (MobileBy.ID, "com.example.mainhomefeed:id/tv_regsiter")
    SIGN_UP = (MobileBy.ID, "com.example.mainhomefeed:id/tv_regsiter")
    HOME_FEED = (MobileBy.ID, "com.example.mainhomefeed:id/homePageViewPager")