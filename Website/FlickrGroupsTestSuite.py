import unittest
import main
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


groups_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order
groups_test_suite.addTest(main.FlickrGroupsTest("test_groups_page_title"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group_no_name"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_group_that_exists"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_create_18_group"))
groups_test_suite.addTest(main.FlickrGroupsTest("test_add_photo_to_group"))




# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker group test").run(groups_test_suite)

# run the suite
