from appium.webdriver.common.mobileby import MobileBy

class PhotoviewPageLocator:
    TITLE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_title_left")
    CLOSE_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_up")
    COMMENT_BUTTON = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_comment_count_left")
    COMMENT_TEXT = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.TextView[2]")
    COMMENT_TEXTBOX = (MobileBy.ID, "com.flickr.android:id/add_comment_content")
    POST_BUTTON = (MobileBy.ID, "com.flickr.android:id/add_comment_post")
    OPTIONS_BUTTON = (MobileBy.ID, "com.flickr.android:id/comments_list_item_menu_icon")
    EDIT_BUTTON = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]")
    DELETE_BUTTON = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")
    COMMENT_TO_EDIT_TEXTBOX = (MobileBy.ID, "com.flickr.android:id/edit_comment_content")
    YES_BUTTON = (MobileBy.ID, "com.flickr.android:id/general_dialog_positive")
    OKAY_BUTTON = (MobileBy.ID, "com.flickr.android:id/fragment_header_action")

