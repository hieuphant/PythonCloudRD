from selenium import webdriver
from hamcrest import assert_that, equal_to
import pytest

from src.Driver.driver import Driver
from src.page_objects.signin_page import SignInPage


class TestDemoClass():
    def setup_class(self):
        # self.driver = webdriver.Remote( command_executor='http://54.254.166.52:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
        self.driver =Driver().make_driver()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://hub.docker.com/sso/start")

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.abc
    def test_title_chars(self):
        assert_that(self.driver.title, equal_to("Docker"))


    def test_demo(self):
        SignInPage(self.driver).enter_user_name("xxx")
        SignInPage(self.driver).enter_user_password("yyy")
        SignInPage(self.driver).click_sign_in_button()
        print("")
