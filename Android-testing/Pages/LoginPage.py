from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.LoginPageLocator import LoginPageLocator
import time

class LoginPage:
    def __init__(self, d):
        self.driver = d

    def enter_email(self, selector):
        if selector == "k":
            email_field = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
            email_field.send_keys("karimamr9@outlook.com")
            next_button = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
            next_button.click()
            self.driver.implicitly_wait(10)
            password = self.driver.find_element(*LoginPageLocator.PASSWORD)
            password.send_keys(",Q#8zUvxmSVJ-L^")
            sign_in = self.driver.find_element(*LoginPageLocator.SIGN_IN)
            sign_in.click()
        elif selector == "m":
            email_field = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
            email_field.send_keys("mohamedamr866@gmail.com")
            next_button = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
            next_button.click()
            self.driver.implicitly_wait(10)
            password = self.driver.find_element(*LoginPageLocator.PASSWORD)
            password.send_keys("abcd12345678")
            sign_in = self.driver.find_element(*LoginPageLocator.SIGN_IN)
            sign_in.click()
        elif selector == "k2":
            email_field = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
            email_field.send_keys("karim_nimo@yahoo.com")
            next_button = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
            next_button.click()
            self.driver.implicitly_wait(10)
            password = self.driver.find_element(*LoginPageLocator.PASSWORD)
            password.send_keys("AVZ7Xf!_SNRBQP2")
            sign_in = self.driver.find_element(*LoginPageLocator.SIGN_IN)
            sign_in.click()


    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def wrong_email_format(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("aaaa")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_warning = self.driver.find_element(*LoginPageLocator.EMAIL_WARNING)
        result = "Hmm… that's not an email address" in email_warning.text
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def no_email(self):
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_required = self.driver.find_element(*LoginPageLocator.EMAIL_REQUIRED)
        return "Required" in email_required.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def right_email(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element(*LoginPageLocator.PASSWORD)
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without the password we will check that the page isn't the home page
    def no_password(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        login.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element(*LoginPageLocator.PROFILE)

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong password "Invalid password" will appear
    def wrong_password(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        login.click()
        self.driver.implicitly_wait(2)
        password_required = self.driver.find_element(*LoginPageLocator.PASSWORD_REQUIRED)
        return "Invalid password" in password_required.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong email and wrong password "Invalid email or password." will appear
    def wrong_email_and_wrong_password(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("karimamr3009@gmail.com")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocator.PASSWORD)
        password.send_keys("abcd12345678")
        login.click()
        self.driver.implicitly_wait(5)
        invalid_email_or_password = self.driver.find_element(*LoginPageLocator.INVALID_EMAIL_OR_PASSWORD)
        return "Invalid email or password." in invalid_email_or_password.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a right email and right password the home page will be reached
    def right_email_and_right_password(self):
        email = self.driver.find_element(*LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocator.PASSWORD)
        password.send_keys("abcd12345678")
        login.click()
        self.driver.implicitly_wait(5)
        result = self.driver.find_element(*LoginPageLocator.PROFILE)
        return result
