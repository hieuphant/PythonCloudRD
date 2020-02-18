from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Driver:

    @staticmethod
    def make_driver():
        chrome_options = Options()
        chrome_options.add_argument('disable-infobars')
        return webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
