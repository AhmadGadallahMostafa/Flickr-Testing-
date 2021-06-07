from Locators.NotificationPageLocator import NotificationPageLocator
import time
class NotificationPage():
    def __init__(self, driver):
        self.driver = driver
    
    def check_last_notification(self):
        last_notification = self.driver.find_element(*NotificationPageLocator.LAST_NOTIFICATION)
        return "karim amr is now following You" in last_notification.text

