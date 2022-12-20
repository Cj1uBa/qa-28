from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AuthLocators:
    Tel_Locat = (By.ID, "t-btn-tab-phone")
    Tel_Active = (By.CSS_SELECTOR, "div#t-btn-tab-phone.rt-tab--active")
    Mail_Locat = (By.ID, "t-btn-tab-mail")
    Mail_Active = (By.CSS_SELECTOR, "div#t-btn-tab-mail.rt-tab--active")
    Login_Locat = (By.ID, "t-btn-tab-login")
    Login_Active = (By.CSS_SELECTOR, "div#t-btn-tab-login.rt-tab--active")
    Phone_Locat = (By.ID, "t-btn-tab-ls")
    Phone_Active = (By.CSS_SELECTOR, "div#t-btn-tab-ls.rt-tab--active")
    User_Locat = (By.ID, "username")
    Phone_Check = (By.CSS_SELECTOR, "span.rt-input-container__meta--error")
    Pas_Locat = (By.ID, "password")
    Enter_Key_Locat = (By.ID, "kc-login")
    Web_Enter_Key_Locat = (By.CLASS_NAME, "go_kab")
    F_Pas_Locat = (By.ID, "forgot_password")
    F_Pas_Active = (By.CSS_SELECTOR, "a#forgot_password.rt-link--orange")
    Error_Locat = (By.ID, "form-error-message")
    Reg_Locat = (By.ID, "kc-register")
    Cap_Locat = (By.CSS_SELECTOR, "div.login-form__captcha")
    Cap_Input_Locat = (By.ID, "captcha")

class AuthPageHelper(BasePage):

    def select_tel_tab(self):
        tel_tab = self.find_element(AuthLocators.Tel_Locat)
        return tel_tab.click()

    def check_Tel_Active(self):
        Tel_Active = self.find_element(AuthLocators.Tel_Active)
        return Tel_Active

    def select_email_tab(self):
        mail_tab = self.find_element(AuthLocators.Mail_Locat)
        return mail_tab.click()

    def check_eMail_Active(self):
        Mail_Active = self.find_element(AuthLocators.Mail_Active)
        return Mail_Active

    def select_login_tab(self):
        login_tab = self.find_element(AuthLocators.Login_Locat)
        return login_tab.click()

    def check_Login_Active(self):
        Login_Active = self.find_element(AuthLocators.Login_Active)
        return Login_Active

    def select_pnumber_tab(self):
        pnumber_tab = self.find_element(AuthLocators.Phone_Locat)
        return pnumber_tab.click()

    def check_Phone_Active(self):
        Phone_Active = self.find_element(AuthLocators.Phone_Active)
        return Phone_Active

    def enter_username(self, username):
        username_field = self.find_element(AuthLocators.User_Locat)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def click_on_password(self):
        return self.find_element(AuthLocators.Pas_Locat).click()

    def enter_password(self, password):
        pswd_field = self.find_element(AuthLocators.Pas_Locat)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_enter_button(self):
        self.find_element(AuthLocators.Enter_Key_Locat).click()

    def keyweb_click_on_enter_button(self):
        return self.find_element(AuthLocators.Web_Enter_Key_Locat).click()

    def click_on_signup_button(self):
        self.find_element(AuthLocators.Reg_Locat).click()

    def click_on_forgot_pswd(self):
        self.find_element(AuthLocators.F_Pas_Locat).click()

    def check_error_message(self):
        return self.find_element(AuthLocators.Error_Locat).text

    def check_phone_format(self):
        return self.find_element(AuthLocators.Phone_Check).text

    def check_captcha(self):
        return self.find_element(AuthLocators.Cap_Locat)

    def click_on_captcha(self):
        self.find_element(AuthLocators.Cap_Input_Locat).click()

    def input_captcha(self, try_captcha):
        captcha = self.find_element(AuthLocators.Cap_Input_Locat)
        captcha.click()
        return captcha.send_keys(try_captcha)









