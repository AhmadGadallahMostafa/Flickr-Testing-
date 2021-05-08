import unittest
import AndroidMain
import HtmlTestRunner

# get all tests from SearchText and HomePageTest class


login_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_email_format'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_email'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_right_email'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_email_and_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_right_email_and_right_password'))







# open the report file


# configure HTMLTestRunner options
#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(login_test_suite)

# run the suite



# get all tests from SearchText and HomePageTest class


logout_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

logout_test_suite.addTest(AndroidMain.FlickrLogoutAndroid('test_logout'))



# open the report file


# configure HTMLTestRunner options
#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(logout_test_suite)

# run the suite

signup_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_first_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_last_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_age'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_email'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_password'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_age'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_email'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_password'))








# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(signup_test_suite)

# run the suite


