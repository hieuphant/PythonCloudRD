from selenium import webdriver
from hamcrest import assert_that, equal_to
import pytest


class TestDemoClass():
    def setup_class(self):
        self.driver = webdriver.Remote( command_executor='http://54.254.166.52:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
        # self.driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
        self.driver.get("https://www.google.com/")

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.abc
    def test_title_chars(self):        
        assert_that(self.driver.title, equal_to("Google"))

    @pytest.mark.xyz
    @pytest.mark.parametrize(
        ('input', 'expected'), [
            (0, 6),
            (1, 7),
            (-1, 5),
        ]
    )
    def test_title_len(self, input, expected):
        assert_that(len(self.driver.title) + input, equal_to(expected))