import unittest
import main
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


upload_test_suite = unittest.TestSuite()


upload_test_suite.addTest(main.FlickerUpload('test_upload_page_title'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_picture'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_multiple_pictures'))
upload_test_suite.addTest(main.FlickerUpload('test_uploaded_picture_in_photostream'))


upload_test_suite.addTest(main.FlickerUpload('test_upload_invalid_type'))
upload_test_suite.addTest(main.FlickerUpload('test_disabled_upload'))
upload_test_suite.addTest(main.FlickerUpload('test_remove_invalid'))
upload_test_suite.addTest(main.FlickerUpload('test_upload_picture'))

# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(upload_test_suite)


# run the suite
