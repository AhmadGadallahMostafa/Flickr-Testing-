from Pages.BasePage import BasePage
from Locators.CameraFinderPageLocators import CameraFinderPageLocators

class CameraFinderPage(BasePage):
    def title_matches(self):
        result = self.driver.title
        return "Camera Finder" in result
    
    def camers_are_loaded(self):
        cameras_list = self.driver.find_elements(*CameraFinderPageLocators.CAMERAS)
        return len(cameras_list)