import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from functions import get_root_path

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
download_path = get_root_path()


@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": r"C:\Users\user\Downloads",
    }
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=service, options=options)


    yield driver
    driver.quit()

