from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import shutil

class BasePageClass:

    def __init__(self):

        webdriver_path = shutil.which("chromedriver")
        service = Service(webdriver_path)
        self.options = ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(service=service,options=self.options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)

