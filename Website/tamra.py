import unittest
import main
import HtmlTestRunner




Signup_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

Signup_test_suite.addTest(main.FlickerSignup('test_firstname'))
Signup_test_suite.addTest(main.FlickerSignup('test_lastname'))
Signup_test_suite.addTest(main.FlickerSignup('test_age'))
Signup_test_suite.addTest(main.FlickerSignup('test_email'))
Signup_test_suite.addTest(main.FlickerSignup('test_password'))
Signup_test_suite.addTest(main.FlickerSignup('test_valid_age'))
Signup_test_suite.addTest(main.FlickerSignup('test_valid_email'))
Signup_test_suite.addTest(main.FlickerSignup('test_valid_password'))



# open the report file


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(Signup_test_suite)

# run the suite






Login_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

Login_test_suite.addTest(main.FlickrLogin('test_wrong_email_format'))
Login_test_suite.addTest(main.FlickrLogin('test_no_email'))
Login_test_suite.addTest(main.FlickrLogin('test_right_email'))
Login_test_suite.addTest(main.FlickrLogin('test_no_password'))
Login_test_suite.addTest(main.FlickrLogin('test_wrong_password'))
Login_test_suite.addTest(main.FlickrLogin('test_wrong_email_and_wrong_password'))
Login_test_suite.addTest(main.FlickrLogin('test_right_email_and_right_password'))



# open the report file


# configure HTMLTestRunner options
#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(Login_test_suite)


Logout_test_suite = unittest.TestSuite()

# Test cases are added manually to ensure their execution order

Logout_test_suite.addTest(main.FlickerLogout('test_logout'))




# open the report file


# configure HTMLTestRunner options
#runner = HtmlTestRunner.HTMLTestRunner(report_name="Flicker valid Upload").run(Logout_test_suite)
