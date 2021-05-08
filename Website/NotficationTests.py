import unittest
import main
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


notification_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
notification_test_suite.addTest(main.FlickrNotifications("test_push"))
notification_test_suite.addTest(main.FlickrNotifications("test_notifications"))


# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker group test").run(notification_test_suite)

# run the suite
