from appium.webdriver.common.mobileby import MobileBy
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
