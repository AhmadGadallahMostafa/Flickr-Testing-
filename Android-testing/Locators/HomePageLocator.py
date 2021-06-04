from appium.webdriver.common.mobileby import MobileBy
class HomePageLocator:
    UPLOAD_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_camera")
    PHOTO_STREAM_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_profile")
    SEARCH_ICON = (MobileBy.ID, "com.flickr.android:id/fragment_navigation_search")
    SEARCH_BOX = (MobileBy.ID, "com.flickr.android:id/search_view_autocompl_textview")
    PEOPLE = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]")
    