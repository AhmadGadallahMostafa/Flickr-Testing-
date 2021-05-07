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


class PhotoViewPageLocator:
    TITLE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_title_left")
    ClOSE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_up")