from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterLocators:
    F_Name_Locat = (By.NAME, "firstName")
    S_Name_Locat = (By.NAME, "lastName")
    Email_Locat = (By.ID, "address")
    Pass1_Locat = (By.ID, "password")
    Pass2_Locat = (By.ID, "password-confirm")
    Reg_B_Locat = (By.NAME, "register")
    Message_Locat = (By.CSS_SELECTOR, "p.register-confirm-form-container__desc")
    List_Locat = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    Value_Locat = (By.CLASS_NAME, "rt-select__list-item")
    Error_Locat = (By.CLASS_NAME, "rt-input-container__meta--error")


class RegPageHelper(BasePage):
    def click_on_first_name(self):
        return self.find_element(RegisterLocators.F_Name_Locat).click()

    def enter_first_name(self, username):
        username_field = self.find_element(RegisterLocators.F_Name_Locat)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_surname(self, surname):
        surname_field = self.find_element(RegisterLocators.S_Name_Locat)
        surname_field.click()
        surname_field.send_keys(surname)
        return surname_field

    def click_on_surname(self):
        return self.find_element(RegisterLocators.S_Name_Locat).click()

    def select_region(self, region_index):
        self.find_element(RegisterLocators.List_Locat).click()
        regions = self.find_elements(RegisterLocators.Value_Locat)
        return regions[region_index].click()

    def enter_email(self, email):
        email_field = self.find_element(RegisterLocators.Email_Locat)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def create_password(self, password):
        pswd_field = self.find_element(RegisterLocators.Pass1_Locat)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_confirm_password(self):
        self.find_element(RegisterLocators.Pass2_Locat).click()

    def confirm_password(self, password2):
        pswd2_field = self.find_element(RegisterLocators.Pass2_Locat)
        pswd2_field.click()
        pswd2_field.send_keys(password2)
        return pswd2_field

    def click_on_register_button(self):
        self.find_element(RegisterLocators.Reg_B_Locat).click()

    def check_confirmation(self):
        return self.find_element(RegisterLocators.Message_Locat).text

    def check_input(self):
        return self.find_element(RegisterLocators.Error_Locat).text