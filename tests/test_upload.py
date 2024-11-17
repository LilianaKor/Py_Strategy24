import time

from data.urls import Urls
from functions import get_root_path
from pages.upload_page import UploadPage


class TestUpload:
    url = Urls()

    def test_upload(self, driver):
        file_path = get_root_path("data/upload/bb.txt")
        page = UploadPage(driver, f"{self.url.herokuapp_base_url}upload")
        page.open()
        page.upload_file(file_path)
        time.sleep(5)
