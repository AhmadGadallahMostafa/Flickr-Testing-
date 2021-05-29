from Pages.BasePage import BasePage
from Locators.PhotostreamPageLocators import PhotoStreamLocators


class PhotoStreamPage(BasePage):
    def picture_title_matches_upload(self, title_uploaded):
        self.driver.implicitly_wait(5)
        title_matches_upload = []
        picture_title = self.driver.find_elements(*PhotoStreamLocators.TITLE)

        for i in range(0, len(picture_title)):
            for j in range(0, len(title_uploaded)):
                if title_uploaded[j] in picture_title[i].get_attribute("title"):
                    title_matches_upload.append(True)
                    break
                else:
                    if j == len(title_uploaded)-1:
                        title_matches_upload.append(False)
        return all(title_matches_upload)
