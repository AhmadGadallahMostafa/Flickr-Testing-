from appium.webdriver.common.mobileby import MobileBy
class GroupPageLocator:
    JOIN_BTN = (MobileBy.ID, "com.flickr.android:id/follow_btn_icon")
    JOIN_STATUS = (MobileBy.ID, "com.flickr.android:id/follow_btn_text")
    THREE_DOTS = (MobileBy.ID, "com.flickr.android:id/group_header_overflow")
    LEAVE = (MobileBy.ID, "com.flickr.android:id/group_options_join_leave")
    CONFIRM_LEAVE = (MobileBy.ID, "com.flickr.android:id/general_dialog_positive")
    ADD_PHOTO = (MobileBy.ID, "com.flickr.android:id/group_options_add_photo")
    PHOTO_LIST = (MobileBy.ID, "com.flickr.android:id/fragment_edit_photos_list")#.//android.view.View
    ADD = (MobileBy.ID, "com.flickr.android:id/fragment_header_action")
    GROUP_PHOTO_LIST = (MobileBy.ID, "com.flickr.android:id/fragment_group_photos_listview")#.//android.widget.ListView/android.widget.LinearLayout/android.view.View
    PHOTO_ADDED_TITLE = (MobileBy.ID, "com.flickr.android:id/activity_lightbox_title_left")