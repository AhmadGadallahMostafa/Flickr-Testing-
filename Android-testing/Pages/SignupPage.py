from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.SignupPageLocator import SignupPageLocator
import time


class SignupPage:
    def __init__(self, d):
        self.driver = d

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def first_name(self):
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        firstname_required = self.driver.find_element(*SignupPageLocator.FIRST_NAME_REQUIRED)
        return "Required" in firstname_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def last_name(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        lastname_required = self.driver.find_element(*SignupPageLocator.LAST_NAME_REQUIRED)
        return "Required" in lastname_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the age it must show the word required to the user
    def age(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        age_required = self.driver.find_element(*SignupPageLocator.AGE_REQUIRED)
        return "Required" in age_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the email it must show the word required to the user
    def email(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        email_required = self.driver.find_element(*SignupPageLocator.EMAIL_REQUIRED)
        return "Required" in email_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the password it must show the word required to the user
    def password(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(10)
        password_required = self.driver.find_element(*SignupPageLocator.PASSWORD_REQUIRED)
        return "Required" in password_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with age less than 13 years it must show "In order to use Flickr, you must be 13 or older"  to the user
    def valid_age(self):
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("9")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        age_warning = self.driver.find_element(*SignupPageLocator.AGE_WARNING)
        return "In order to use Flickr, you must be 13 or older" in age_warning.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with an email in a wrong format it must show "Invalid email"  to the user
    def valid_email(self):
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866gmail.com")
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        email_warning = self.driver.find_element(*SignupPageLocator.EMAIL_WARNING)
        return "Invalid email" in email_warning.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with a password less than 12 charachters  it must show "Invalid password"  to the user
    def valid_password(self):
        down = self.driver.find_element(*SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        password_warning = self.driver.find_element(*SignupPageLocator.PASSWORD_WARNING)
        print(password_warning.text)
        return "Invalid password" in password_warning.text
