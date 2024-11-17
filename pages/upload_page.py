from pages.base_page import BasePage
from locators.upload_page_herokuapp_locators import UploadPageLocators

class UploadPage(BasePage):
    locators = UploadPageLocators

    def upload_file(self, file_path):
        self.element_is_visible(self.locators.UPLOAD_loc).send_keys(file_path)
