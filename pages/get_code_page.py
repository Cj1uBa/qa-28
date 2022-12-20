from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class GetCodeLocators():
    But_Locat = (By.ID, "otp_get_code")
    ENTER_WITH_PSWD_BUTTON_LOCATOR = (By.ID, "standard_auth_btn")
    Back_Button_Locat = (By.ID, "back_to_otp_btn")
    Dig_Locat = (By.CSS_SELECTOR, "div.sdi-container--medium")
    Input_Locat = (By.CSS_SELECTOR, "input.code-input__input")
    C_Email_Locat = (By.NAME, "otp_back_phone")
    Timeout_Locat = (By.CSS_SELECTOR, "span.code-input-container__timeout")
    Page_Locat = (By.CSS_SELECTOR, "h1.card-container__title")
    Exelent_Title = (By.CSS_SELECTOR, "h1.card-container__title")
    Exelent_Message = (By.CSS_SELECTOR, "p.otp-code-form-container__desc")
    Error_Message = (By.CSS_SELECTOR, "p.card-container__error")


class GetCodePageHelper(BasePage):
    def click_on_enter_with_pswd_button(self):
        return self.find_element(GetCodeLocators.ENTER_WITH_PSWD_BUTTON_LOCATOR).click()

    def click_on_back_to_one_time_code(self):
        return self.find_element(GetCodeLocators.Back_Button_Locat).click()

    def click_on_get_code(self):
        self.find_element(GetCodeLocators.But_Locat).click()

    def check_error_message(self):
        return self.find_element(GetCodeLocators.Error_Message).text

    def keyweb_check_page_title(self):
        return self.find_element(GetCodeLocators.Page_Locat).text

    def check_code_input_field(self):
        return self.find_element(GetCodeLocators.Dig_Locat)

    def enter_one_time_code(self, code):
        code_input = self.find_element(GetCodeLocators.Input_Locat)
        return code_input.send_keys(code)

    def check_change_email_link(self):
        return self.find_element(GetCodeLocators.C_Email_Locat).text

    def check_countdown(self):
        return self.find_element(GetCodeLocators.Timeout_Locat).text

    def check_Exelent_Title(self):
        return self.find_element(GetCodeLocators.Exelent_Title).text

    def check_Exelent_Message(self):
        return self.find_element(GetCodeLocators.Exelent_Message).text