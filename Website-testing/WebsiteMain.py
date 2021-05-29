import unittest
from selenium import webdriver
from Pages.MainPage import MainPage
from Pages.GroupsPage import GroupsPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage
from Pages.NotificationPage import NotificationPage
from Pages.PhotostreamPage import PhotoStreamPage
from Pages.PrintsPage import PrintsPage
from Pages.MainPage import MainPage
from Pages.SignupPage import SignupPage
from Pages.UploadPage import UploadPage

import time


def login(driver):
    main_page = MainPage(driver)
    main_page.click_login_button()
    loginPage = LoginPage(driver)
    loginPage.email_text = "karimamr9@outlook.com"
    loginPage.go_next()
    loginPage.password_text = ",Q#8zUvxmSVJ-L^"
    loginPage.go_next()
    

class FlickerUpload(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
        login(inst.driver)
        inst.titles = []

    def test_upload_page_title(self):
        home_page = HomePage(self.driver)
        self.driver.implicitly_wait(5)
        home_page.go_upload()
        upload_page = UploadPage(self.driver)
        self.assertTrue(upload_page.title_matches())

    def test_upload_picture(self):
        upload_age = UploadPage(self.driver)
        files = ["p1.jpg"]
        self.titles.append("p1")
        upload_age.choose_file(files)
        self.driver.implicitly_wait(3)
        self.assertTrue(upload_age.confirm_upload())

    def test_upload_multiple_pictures(self):
        home_page = HomePage(self.driver)
        home_page.go_upload()
        self.driver.implicitly_wait(5)
        upload_age = UploadPage(self.driver)
        files = ["p2.png", "p3.png", "p4.jpg"]
        self.titles.append("p2")
        self.titles.append("p3")
        self.titles.append("p4")
        upload_age.choose_file(files)
        self.driver.implicitly_wait(3)
        self.assertTrue(upload_age.confirm_upload())

    # test edit photo info later

    def test_uploaded_picture_in_photostream(self):
        time.sleep(5)
        photo_stream_page = PhotoStreamPage(self.driver)
        self.assertTrue(photo_stream_page.picture_title_matches_upload(self.titles))
        

    def test_upload_invalid_type(self):
        upload_age = UploadPage(self.driver)
        files = ["invalid.pdf"]
        upload_age.choose_file(files)
        self.assertTrue(upload_age.detects_invalid())

    def test_upload_large_file(self):
        upload_age = UploadPage(self.driver)
        file = ["large.mp4"]
        upload_age.choose_file(file)
        self.assertTrue(upload_age.detects_invalid())
        upload_age.remove_invalid()

    def test_disabled_upload(self):
        upload_age = UploadPage(self.driver)
        self.driver.implicitly_wait(5)
        with self.assertRaises(Exception) as context:
            upload_age.confirm_upload()

    def test_remove_invalid(self):
        upload_age = UploadPage(self.driver)
        upload_age.remove_invalid()
        self.assertFalse(upload_age.detects_invalid())

    def test_close_before_uploading(self):
        home = HomePage(self.driver)
        self.driver.implicitly_wait(5)
        home.go_upload()
        self.driver.implicitly_wait(5)
        upload_age = UploadPage(self.driver)
        upload_age.choose_file(["never.mkv"])
        upload_age.cancel_upload()
        self.setUpClass()
        self.driver.implicitly_wait(5)
        home = HomePage(self.driver)
        home.go_to_photostream()
        photo_stream_page = PhotoStreamPage(self.driver)
        title = ["never"]
        self.assertFalse(photo_stream_page.picture_title_matches_upload(title))



    @classmethod
    def tearDownClass(inst):
        inst.driver.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------

class FlickrLogin(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        login = inst.driver.find_element_by_link_text("Log In")
        login.click()

    def test_wrong_email_format(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.wrong_email_format())

    def test_no_email(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.no_email())

    def test_right_email(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.right_email())

    def test_no_password(self):
        login_page = LoginPage(self.driver)
        self.assertFalse(login_page.no_password())

    def test_wrong_password(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.wrong_password())

    def test_wrong_email_and_wrong_password(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.wrong_email_and_wrong_password())

    def test_right_email_and_right_password(self):
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.right_email_and_right_password())


    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


class FlickerLogout(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        login = inst.driver.find_element_by_link_text("Log In")
        login.click()
        email = inst.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = inst.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(3)
        password = inst.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = inst.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(3)

    def test_logout(self):
        logout_page = LogoutPage(self.driver)
        self.assertTrue(logout_page.logout())


    @classmethod
    def tearDownClass(inst):
        inst.driver.close()

class FlickerSignup(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        signup = inst.driver.find_element_by_link_text("Sign Up")
        signup.click()

    def test_firstname(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.firstname())

    def test_lastname(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.lastname())

    def test_age(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.age())

    def test_email(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.email())

    def test_password(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.password())

    def test_valid_age(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.valid_age())

    def test_valid_email(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.valid_email())

    def test_valid_password(self):
        signup_page = SignupPage(self.driver)
        self.assertTrue(signup_page.valid_password())

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()



class FlickrGroupsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
        login(inst.driver)
        home_page = HomePage(inst.driver)
        home_page.go_to_groups()

    def test_groups_page_title(self):
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.title_matches())

    def test_create_group_no_name(self):
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.create_group_no_name())
        
    def test_create_group(self):
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.create_group())
    
    def test_create_group_that_exists(self):
        home_page = HomePage(self.driver)
        home_page.go_to_groups()
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.create_group_that_exists())

    def test_create_18_group(self):
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.create_18_age_group())

    def test_add_photo_to_group(self):
        home_page = HomePage(self.driver)
        home_page.go_to_groups()
        groups_page = GroupsPage(self.driver)
        self.assertTrue(groups_page.add_photo_to_group())

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()



class FlickrNotifications(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        #first send open second account and send notification to main acc
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
        main_page = MainPage(inst.driver)
        main_page.click_login_button()
        loginPage = LoginPage(inst.driver)
        loginPage.email_text = "karim_nimo@yahoo.com"
        loginPage.go_next()
        loginPage.password_text = "AVZ7Xf!_SNRBQP2"
        loginPage.go_next()
        home_page = HomePage(inst.driver)
        time.sleep(5)
        home_page.send_notification()
        inst.driver.close()
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
        login(inst.driver)

    def test_push(self):
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.check_push_notifications())

    def test_notifications(self):
        notification_page = NotificationPage(self.driver)
        self.assertTrue(notification_page.check_last_notficiation())

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()

class FlikcrPrints(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
        login(inst.driver)
        home_page = HomePage(inst.driver)
        time.sleep(5)
        home_page.go_to_prints()
    
    def test_prints_title(self):
        prints_page = PrintsPage(self.driver)
        self.assertTrue(prints_page.title_matches())

    def test_choose_photo(self):
        prints_page = PrintsPage(self.driver)
        self.assertTrue(prints_page.choose_photo())

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()

