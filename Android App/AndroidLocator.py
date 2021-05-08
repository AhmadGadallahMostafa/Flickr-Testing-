from appium.webdriver.common.mobileby import MobileBy


class WelcomePageLocator:
    GET_STARTED = (MobileBy.ACCESSIBILITY_ID, "Get Started")


class LoginPageLocator:
    EMAIL_FIELD = (MobileBy.ID, "login-email")
    NEXT_BUTTON = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
    PASSWORD = (MobileBy.ID, "login-password")
    SIGN_IN = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
    EMAIL_WARNING = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
    EMAIL_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View")
    PASSWORD_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[2]/android.view.View")
    INVALID_EMAIL_OR_PASSWORD = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]")
    PROFILE = (MobileBy.ACCESSIBILITY_ID, "Profile")

class HomePageLocator:
    UPLOAD_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_camera")
    PHOTO_STREAM_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_profile")


class UploadPageLocator:
    PERMISSION_BLOCK = (MobileBy.ID, "com.android.permissioncontroller:id/content_container")
    ALLOW = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    CAMERA_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_camera_capture_btn")
    NEXT_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_image_editor_next")
    POST_BUTTON = (MobileBy.ID ,"com.flickr.android:id/fragment_header_action")
    TITLE_TEXT = (MobileBy.ID, "com.flickr.android:id/activity_media_upload_title")
    GALLERY_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_camera_gallery_btn")
    DOWNLOADS = (MobileBy.ID, "com.flickr.android:id/bucketIcon")
    PICKER_GRID = (MobileBy.ID, "com.flickr.android:id/picker_grid_image")
    DONE = (MobileBy.ID, "com.flickr.android:id/actionbar_button")


class PhotoStreamPageLocator:
    MESSAGE_BAR = (MobileBy.ID, "com.flickr.android:id/snackbar_text")
    PICTURE_BOX = (MobileBy.ID, "com.flickr.android:id/square_photo_view")
    DATE_LIST = (MobileBy.ID, "com.flickr.android:id/fragment_camera_roll_header_date_mode_text")
    DATE_UPLOADED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")


class PhotoViewPageLocator:
    TITLE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_title_left")
    CLOSE_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_up")

class LogoutPageLocator:
    PROFILE = (MobileBy.ACCESSIBILITY_ID, "Profile")
    SETTINGS = (MobileBy.ID, "com.flickr.android:id/profile_header_overflow")
    SIGNOUT = (MobileBy.ID, "com.flickr.android:id/profile_settings_logout")
    GET_STARTED = (MobileBy.ACCESSIBILITY_ID, "Get Started")

class SignupPageLocator:
    FIRST_NAME = (MobileBy.ID, "sign-up-first-name")
    LAST_NAME = (MobileBy.ID, "sign-up-last-name")
    AGE = (MobileBy.ID, "sign-up-age")
    EMAIL = (MobileBy.ID, "sign-up-email")
    PASSWORD = (MobileBy.ID, "sign-up-password")
    SIGNUP = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
    FIRST_NAME_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View")
    LAST_NAME_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View")
    AGE_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View")
    EMAIL_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View")
    PASSWORD_REQUIRED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View")
    AGE_WARNING = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View")
    EMAIL_WARNING = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View")
    PASSWORD_WARNING = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View")
    DOWN = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Image")


