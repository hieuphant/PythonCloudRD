from src.page_objects.locators.signin_page_locators import *
from src.page_objects.page import BasePage


class SignInPage(BasePage):

    def enter_user_name(self, value):
        self.type_text(username_txt, value)

    def enter_user_password(self, value):
        self.type_text(pwd_txt, value)

    def click_sign_in_button(self):
        self.click_element(sign_in_btn)
