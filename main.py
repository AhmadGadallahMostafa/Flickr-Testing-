import unittest
from selenium import webdriver
import page
import time


def login(driver):
    mainPage = page.MainPage(driver)
    mainPage.click_login_button()
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
        homePage = page.HomePage(inst.driver)
        inst.driver.implicitly_wait(5)
        inst.titles = []
        homePage.go_upload()

    def test_upload_page_title(self):
        uploadPage = page.UploadPage(self.driver)
        assert uploadPage.title_matches()

    def test_upload_picture(self):
        uploadPage = page.UploadPage(self.driver)
        files = ["p1.jpg"]
        self.titles.append("p1")
        uploadPage.choose_file(files)
        self.driver.implicitly_wait(3)
        uploadPage.confirm_upload()
        assert uploadPage.complete_upload_confirmation()

    def test_upload_multiple_pictures(self):
        homePage = page.HomePage(self.driver)
        homePage.go_upload()
        self.driver.implicitly_wait(3)
        uploadPage = page.UploadPage(self.driver)
        files = ["p2.png", "p3.png", "p4.jpg"]
        self.titles.append("p2")
        self.titles.append("p3")
        self.titles.append("p4")
        uploadPage.choose_file(files)
        self.driver.implicitly_wait(3)
        uploadPage.confirm_upload()
        assert uploadPage.complete_upload_confirmation()

    # test edit photo info later

    def test_uploaded_picture_in_photostream(self):
        photoStreamPage = page.PhotoStreamPage(self.driver)
        assert photoStreamPage.picture_title_matches_upload(self.titles)

# -------------------------------------------------------------------------------------------------------------------------------------------------

    def test_upload_invalid_type(self):
        uploadPage = page.UploadPage(self.driver)
        uploadPage.choose_file("invalid.pdf")
        assert uploadPage.detects_invalid()

    def test_upload_large_file(self):
        uploadPage = page.UploadPage(self.driver)
        uploadPage.choose_file("large")
        assert uploadPage.detects_invalid()

    def test_disabled_upload(self):
        uploadPage = page.UploadPage(self.driver)
        self.driver.implicitly_wait(5)
        with self.assertRaises(Exception) as context:
            uploadPage.confirm_upload()

    def test_remove_invalid(self):
        uploadPage = page.UploadPage(self.driver)
        uploadPage.remove_invalid()
        self.assertFalse(uploadPage.detects_invalid())

    def test_close_before_uploading(self):
        pass

    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()
