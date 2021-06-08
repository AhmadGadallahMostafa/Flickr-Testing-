from appium.webdriver.common.mobileby import MobileBy
class SignupPageLocator:
    FIRST_NAME = (MobileBy.ID, "com.example.mainhomefeed:id/et_name")
    LAST_NAME = (MobileBy.ID, "com.example.mainhomefeed:id/et_sname")
    AGE = (MobileBy.ID, "com.example.mainhomefeed:id/et_Age")
    EMAIL = (MobileBy.ID, "com.example.mainhomefeed:id/et_email")
    PASSWORD = (MobileBy.ID, "com.example.mainhomefeed:id/et_pass")
    REPEATE_PASS = (MobileBy.ID, "com.example.mainhomefeed:id/et_rep_pass")
    SIGNUP = (MobileBy.ID, "com.example.mainhomefeed:id/button_register")


