import unittest
import AndroidMain
import HtmlTestRunner


login_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_email'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_no_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_wrong_email_and_wrong_password'))
login_test_suite.addTest(AndroidMain.FlickrLoginAndroid('test_right_email_and_right_password'))


#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Login",report_title="Login Android Tests",combine_reports=True).run(login_test_suite)
# ===============================================================================================================================
signup_test_suite = unittest.TestSuite()

signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_first_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_last_name'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_age'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_email'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_password'))
signup_test_suite.addTest(AndroidMain.FlickrSignupAndroid('test_valid_password'))


runner = HtmlTestRunner.HTMLTestRunner(report_name="Flickr Android Signup",report_title="Signup Android Tests",combine_reports=True).run(signup_test_suite)
