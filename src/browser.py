import platform
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver(headless=True):
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    system = platform.system()

    if system == "Windows":
        driver_path = "drivers/chromedriver.exe"
        browser_path = "browser/chrome-win64/chrome.exe"
    else:
        driver_path = "drivers/chromedriver"
        browser_path = "browser/chrome-linux64/chrome"

    options.binary_location = str(Path(browser_path).resolve())

    service = Service(str(Path(driver_path).resolve()))

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver