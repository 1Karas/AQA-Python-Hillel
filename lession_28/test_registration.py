import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
import shutil
from lession_28.login_page import LoginPage

class PageClass:
    def __init__(self):

        webdriver_path = shutil.which("chromedriver")
        service = Service(webdriver_path)
        self.options = ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=service, options=self.options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
    def quit(self):
        self.driver.quit()


@pytest.fixture()
def driver():

    base_page = PageClass()
    yield base_page.driver
    base_page.quit()


@pytest.fixture()
def login_page(driver):
    login_url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
    driver.get(login_url)
    return LoginPage(driver)


def test_user_registration(login_page):

    login_page.open_registration_form()

    login_page.register_user(
        email="tesstuserss@example.com",
        password="Password123",
        name="Test",
        surname="User"
    )
    assert login_page.verify_success_message(), "Registration was not successful."

