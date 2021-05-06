from appium.webdriver.common.mobileby import MobileBy


class WelcomePageLocator:
    GET_STARTED = (MobileBy.ACCESSIBILITY_ID, "Get Started")


class LoginPageLocator:
    EMAIL_FIELD = (MobileBy.ID, "login-email")
    NEXT_BUTTON = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
    PASSWORD = (MobileBy.ID, "login-password")
    SIGN_IN = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")


class HomePageLocator:
    UPLOAD_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_camera")


class UploadPageLocator:
    PERMISSION_BLOCK = (MobileBy.ID, "com.android.permissioncontroller:id/content_container")
    ALLOW = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
