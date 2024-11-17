from pages.base_page import BasePage
from locators.download_page_herokuapp_locators import DownloadPageLocators


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_loc).click()