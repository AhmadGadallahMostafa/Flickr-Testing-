import unittest
import AndroidMain
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


upload_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_upload_activity'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_take_picture'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_photo_from_camera_in_photo_stream'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_from_gallery'))
upload_test_suite.addTest(AndroidMain.FlickrUploadAndroid('test_photo_from_gallery_in_photo_stream'))




# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker Android Upload").run(upload_test_suite)

# run the suite
