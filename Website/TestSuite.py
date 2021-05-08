import unittest
import main
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


upload_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

upload_test_suite.addTest(main.FlickerUpload('test_upload_page_title'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_large_file'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_invalid_type'))
upload_test_suite.addTest(main.FlickerUpload('test_disabled_upload'))
upload_test_suite.addTest(main.FlickerUpload('test_remove_invalid'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_picture'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_multiple_pictures'))
upload_test_suite.addTest(main.FlickerUpload('test_uploaded_picture_in_photostream'))
upload_test_suite.addTest(main.FlickerUpload('test_close_before_uploading'))


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload", combine_reports=True).run(upload_test_suite)



groups_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
groups_test_suite.addTest(main.FlickrGroupsTest("test_groups_page_title"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group_no_name"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_add_photo_to_group"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group_that_exists"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_18_group"))



# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker group test",combine_reports=True).run(groups_test_suite)


notification_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
notification_test_suite.addTest(main.FlickrNotifications("test_push"))
notification_test_suite.addTest(main.FlickrNotifications("test_notifications"))


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker notification test",combine_reports=True).run(notification_test_suite)


