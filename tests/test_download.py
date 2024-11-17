from pages.download_page import DownloadPage
from data.urls import Urls


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        page = DownloadPage(driver, f"{self.url.herokubase_url}/download")
