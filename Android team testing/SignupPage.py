from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from SignupPageLocator import SignupPageLocator
import time


class SignupPage:
    def __init__(self, d):
        self.driver = d

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def first_name(self):
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        self.driver.back()
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(3)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def last_name(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(3)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the age it must show the word required to the user
    def age(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        self.driver.back()
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the email it must show the word required to the user
    def email(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        self.driver.back()
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)


    # Tester: Mohamed Amr
    # This function tests if we try to signup without the password it must show the word required to the user
    def password(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        self.driver.back()
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        self.driver.back()
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(10)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)

    
    # Tester: Mohamed Amr
    # This function tests if we try to signup with a password less than 10 charachters  it must show "Invalid password"  to the user
    def valid_password(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        self.driver.back()
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        self.driver.back()
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
    

    def signup_completed(self):
        firstname = self.driver.find_element(*SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        self.driver.back()
        lastname = self.driver.find_element(*SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        self.driver.back()
        age = self.driver.find_element(*SignupPageLocator.AGE)
        age.send_keys("20")
        self.driver.back()
        email = self.driver.find_element(*SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaaaaaa")
        self.driver.back()
        rep_password = self.driver.find_element(*SignupPageLocator.REPEATE_PASS)
        rep_password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        signup = self.driver.find_element(*SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        

    
        