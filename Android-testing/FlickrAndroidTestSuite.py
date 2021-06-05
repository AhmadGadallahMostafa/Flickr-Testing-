import unittest
import AndroidMain
import HtmlTestRunner


login_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_email_format'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_email'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_right_email'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_email_and_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_right_email_and_right_password'))

#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Login",report_title="Login Android Tests",combine_reports=True).run(login_test_suite)
# ===============================================================================================================================

logout_test_suite = unittest.TestSuite()

logout_test_suite.addTest(AndroidMain.FlickrLogoutAndroid('test_logout'))


#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Logout",report_title="Logout Android Tests",combine_reports=True).run(logout_test_suite)

#================================================================================
signup_test_suite = unittest.TestSuite()

signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_first_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_last_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_age'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_email'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_password'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_age'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_email'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_password'))

#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Signup",report_title="Signup Android Tests",combine_reports=True).run(signup_test_suite)

#========================================================================
upload_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_upload_activity'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_take_picture'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_photo_from_camera_in_photo_stream'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_from_gallery'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_photo_from_gallery_in_photo_stream'))


#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Upload",report_title="Upload Android",combine_reports=True).run(upload_test_suite)
#========================================================================
view_photo_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
view_photo_test_suite.addTest(AndroidMain.FlickrViewPhotoAndroid('test_view_photo'))

#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android View Photo", report_title="View Photo Android", combine_reports=True).run(view_photo_test_suite)
#=========================================================
profile_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

profile_test_suite.addTest(AndroidMain.FlickrProfileAndroid('test_follow'))
profile_test_suite.addTest(AndroidMain.FlickrProfileAndroid('test_unfollow'))


#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Profile",report_title="Flickr Profile", combine_reports=True).run(profile_test_suite)
#==============================================================

group_test_suite = unittest.TestSuite()

group_test_suite.addTest(AndroidMain.FlickGroupAndroid("test_join_group"))
group_test_suite.addTest(AndroidMain.FlickGroupAndroid("test_add_photo_to_group"))
group_test_suite.addTest(AndroidMain.FlickGroupAndroid("test_leave_group"))


runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Groups",report_title="Flickr Groups", combine_reports=True).run(group_test_suite)
#===============================================================


comment_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

comment_test_suite.addTest(AndroidMain.FlickrCommentsAndroid('test_comment'))
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Comment", report_title="Comment Android", combine_reports=True).run(comment_test_suite)


