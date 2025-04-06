import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.download_page import DownloadPage
from data.urls import Urls


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        page = DownloadPage(driver, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
        time.sleep(5)


def test_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.find_element(By.ID, 'dropdown').click()
    driver.find_element(By.XPATH, "//option[@value='1']").click()
    assert driver.find_element(By.ID, 'dropdown').get_attribute('value') == '1'
    driver.quit()