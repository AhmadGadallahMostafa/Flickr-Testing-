from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.PhotostreamPageLocator import PhotostreamPageLocator
from Locators.PhotoviewPageLocator import PhotoviewPageLocator
from Locators.HomePageLocator import HomePageLocator
import time

class PhotostreamPage:
    def __init__(self, d):
        self.driver = d

    def comment(self):
