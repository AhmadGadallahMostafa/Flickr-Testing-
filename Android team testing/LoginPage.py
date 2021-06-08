from LoginPageLocators import LoginPageLocators
import time

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
    
    def login_with_new_acc(self):
        email_field = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys("mohamedamr866@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaaaaaa")
        self.driver.back()
        sign_in = self.driver.find_element(*LoginPageLocators.SIGNUP_BTN)
        sign_in.click()
        time.sleep(5)
        home_feed = self.driver.find_element(*LoginPageLocators.HOME_FEED)
        
    def no_email(self):
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("asd12345678")
        self.driver.back()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login.click()
        time.sleep(3)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def no_password(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys("Karimamr9@outlook.com")
        self.driver.back()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login.click()
        time.sleep(3)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def wrong_password(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys("Karimamr9@outlook.com")
        self.driver.back()
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        self.driver.back()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login.click()
        time.sleep(5)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
    
    def wrong_email_and_wrong_password(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys("karimamr3009@gmail.com")
        self.driver.back()
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("134502851dasad")
        self.driver.back()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login.click()
        time.sleep(5)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def right_email_and_right_password(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys("Karimamr9@outlook.com")
        self.driver.back()
        password = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("asd12345678")
        self.driver.back()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        login.click()
        time.sleep(5)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)


        
