from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RecoveryLocators:
    Next_Locat = (By.ID, "reset")
    Logo_Locat = (By.CSS_SELECTOR, "svg.main-header__logo")
    Cap_Locat = (By.CSS_SELECTOR, "div.rt-captcha__image-con")

class RecoveryPageHelper(BasePage):
    def click_on_continue_button(self):
        return self.find_element(RecoveryLocators.Next_Locat).click()

    def click_on_main_logo(self, value):
        return self.find_element(RecoveryLocators.Logo_Locat).click()

    def check_captcha(self):
        return self.find_element(RecoveryLocators.Cap_Locat)