import unittest
from selenium import webdriver
import page
import time


def login(driver):
    main_page = page.MainPage(driver)
    main_page.click_login_button()
    loginPage = page.LoginPage(driver)
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
        home_page = page.HomePage(self.driver)
        self.driver.implicitly_wait(5)
        home_page.go_upload()
        upload_age = page.UploadPage(self.driver)
        self.assertTrue(upload_age.title_matches())

    def test_upload_picture(self):
        upload_age = page.UploadPage(self.driver)
        files = ["p1.jpg"]
        self.titles.append("p1")
        upload_age.choose_file(files)
        self.driver.implicitly_wait(3)
        self.assertTrue(upload_age.confirm_upload())

    def test_upload_multiple_pictures(self):
        home_page = page.HomePage(self.driver)
        home_page.go_upload()
        self.driver.implicitly_wait(5)
        upload_age = page.UploadPage(self.driver)
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
        photo_stream_page = page.PhotoStreamPage(self.driver)
        self.assertTrue(photo_stream_page.picture_title_matches_upload(self.titles))

# -------------------------------------------------------------------------------------------------------------------------------------------------

    def test_upload_invalid_type(self):
        upload_age = page.UploadPage(self.driver)
        files = ["invalid.pdf"]
        upload_age.choose_file(files)
        self.assertTrue(upload_age.detects_invalid())

    def test_upload_large_file(self):
        upload_age = page.UploadPage(self.driver)
        file = ["large.mp4"]
        upload_age.choose_file(file)
        self.assertTrue(upload_age.detects_invalid())
        upload_age.remove_invalid()

    def test_disabled_upload(self):
        upload_age = page.UploadPage(self.driver)
        self.driver.implicitly_wait(5)
        with self.assertRaises(Exception) as context:
            upload_age.confirm_upload()

    def test_remove_invalid(self):
        upload_age = page.UploadPage(self.driver)
        upload_age.remove_invalid()
        self.assertFalse(upload_age.detects_invalid())

    def test_close_before_uploading(self):
        home = page.HomePage(self.driver)
        self.driver.implicitly_wait(5)
        home.go_upload()
        self.driver.implicitly_wait(5)
        upload_age = page.UploadPage(self.driver)
        upload_age.choose_file(["never.mkv"])
        upload_age.cancel_upload()
        self.setUpClass()
        self.driver.implicitly_wait(5)
        home = page.HomePage(self.driver)
        home.go_to_photostream()
        photo_stream_page = page.PhotoStreamPage(self.driver)
        title = ["never"]
        self.assertFalse(photo_stream_page.picture_title_matches_upload(title))

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()
