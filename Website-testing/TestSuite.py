import unittest
import WebsiteMain
import HtmlTestRunner



Signup_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_firstname'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_lastname'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_age'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_email'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_password'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_valid_age'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_valid_email'))
Signup_test_suite.addTest(WebsiteMain.FlickerSignup('test_valid_password'))

runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker Signup tests",report_title="Signup test", combine_reports = True).run(Signup_test_suite)
#===========================================================================================================================

Login_test_suite = unittest.TestSuite()

Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_wrong_email_format'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_no_email'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_right_email'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_no_password'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_wrong_password'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_wrong_email_and_wrong_password'))
Login_test_suite.addTest(WebsiteMain.FlickrLogin('test_right_email_and_right_password'))

runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker Login tests",report_title="Login test", combine_reports = True).run(Login_test_suite)

#===========================================================================================================================
Logout_test_suite = unittest.TestSuite()

Logout_test_suite.addTest(WebsiteMain.FlickerLogout('test_logout'))

runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker Logout tests",report_title="Logout test", combine_reports = True).run(Logout_test_suite)
#===========================================================================================================================
upload_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_upload_page_title'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_upload_large_file'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_upload_invalid_type'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_disabled_upload'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_remove_invalid'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_upload_picture'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_upload_multiple_pictures'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_uploaded_picture_in_photostream'))
upload_test_suite.addTest(WebsiteMain.FlickerUpload('test_close_before_uploading'))


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker  Upload",report_title="Upload test", combine_reports=True).run(upload_test_suite)
#===========================================================================================================================
groups_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_groups_page_title"))
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_create_group_no_name"))
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_create_group"))
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_add_photo_to_group"))
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_create_group_that_exists"))
groups_test_suite.addTest(WebsiteMain.FlickrGroupsTest("test_create_18_group"))



# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker group test",report_title="Groups test",combine_reports=True).run(groups_test_suite)
#===========================================================================================================================
notification_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
notification_test_suite.addTest(WebsiteMain.FlickrNotifications("test_push"))
notification_test_suite.addTest(WebsiteMain.FlickrNotifications("test_notifications"))

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker notification test",report_title="Notifications test",combine_reports=True).run(notification_test_suite)
#===========================================================================================================================
prints_test_suite = unittest.TestSuite()

prints_test_suite.addTest(WebsiteMain.FlikcrPrints('test_prints_title'))
prints_test_suite.addTest(WebsiteMain.FlikcrPrints("test_choose_photo"))

runner = HtmlTestRunner.HTMLTestRunner(report_name="Prints",report_title="Prints test",combine_reports=True).run(prints_test_suite)
