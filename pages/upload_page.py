from pages.base_page import BasePage
from locators.upload_page_herokuapp_locators import UploadPageLocators


class UploadPage(BasePage):
    locators = UploadPageLocators

    def upload_file(self, file_path):
        self.element_is_visible(self.locators.UPLOAD_loc).send_keys(file_path)
        self.element_is_clickable(self.locators.SUBMIT_loc).click()

    def check_upload_file(self):
        h3_text = self.element_is_visible(self.locators.HEADER_TEXT_loc).text
        file_name = self.element_is_visible(self.locators.UPLOADED_FILE_loc).text
        return h3_text,file_name



