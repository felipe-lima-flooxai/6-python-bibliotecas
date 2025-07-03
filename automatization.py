from pathlib import Path
from time import sleep
from selenium import wbdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chromedriver.exe"


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=CHROMEDRIVER_DRIVER_PATH)

    chrome_browser = webdriver.Chrome(
                        service = chrome_service,
                        options = chrome_options                 
                    )
    
    return browser

if __name__ == "__main__":
    options = ("--disable-gpu", "--no-sandbox")
    browser = make_chrome_browser(*options)

chrome_browser.get("https://www.google.com.br/")
