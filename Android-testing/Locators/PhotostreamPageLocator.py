from appium.webdriver.common.mobileby import MobileBy
class PhotostreamPageLocator:
    MESSAGE_BAR = (MobileBy.ID, "com.flickr.android:id/snackbar_text")
    PICTURE_BOX = (MobileBy.ID, "com.flickr.android:id/square_photo_view")
    DATE_LIST = (MobileBy.ID, "com.flickr.android:id/fragment_camera_roll_header_date_mode_text")
    DATE_UPLOADED = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")

