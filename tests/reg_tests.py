import pytest
from pages.reg_page import RegPageHelper
from test_data import TestDataSet


@pytest.mark.parametrize("surname", TestDataSet.wrong_name, ids=TestDataSet.wrong_name_ids)
def test_elk_sign_up_invalid_surname(browser, elk_open_sign_up_page, surname):
    reg_page = RegPageHelper(browser)
    reg_page.enter_surname(surname)
    if surname == "":
        reg_page.enter_first_name("Дмитрий")
        email = "sliva997@mail"
        reg_page.enter_email(email)
        reg_page.create_password("399R8gSliva")
        reg_page.confirm_password("399R8gSliva")
        reg_page.click_on_register_button()
    else:
        reg_page.click_on_first_name()
    assert reg_page.check_input() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

@pytest.mark.parametrize("first_name", TestDataSet.wrong_name, ids=TestDataSet.wrong_name_ids)
def test_elk_sign_up_invalid_first_name(browser, elk_open_sign_up_page, first_name):
    reg_page = RegPageHelper(browser)
    reg_page.enter_first_name(first_name)
    if first_name == "":
        reg_page.enter_surname("Сливный")
        email = "sliva997@mail"
        reg_page.enter_email(email)
        reg_page.create_password("399R8gSliva")
        reg_page.confirm_password("399R8gSliva")
        reg_page.click_on_register_button()
    else:
        reg_page.click_on_surname()
    assert reg_page.check_input() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.parametrize("username", TestDataSet.invalid_phone_or_email, ids=TestDataSet.invalid_phone_or_email_ids)
def test_elk_sign_up_invalid_phone_or_email(browser, elk_open_sign_up_page, username):
    reg_page = RegPageHelper(browser)
    reg_page.enter_email(username)
    if username == "":
        reg_page = RegPageHelper(browser)
        reg_page.enter_first_name("Дмитрий")
        reg_page.enter_surname("Сливный")
        reg_page.create_password("399R8gSliva")
        reg_page.confirm_password("399R8gSliva")
    else:
        pass
    reg_page.click_on_register_button()
    assert reg_page.check_input() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email " \
                                     "в формате example@email.ru"


@pytest.mark.parametrize("password", TestDataSet.invalid_pswd, ids=TestDataSet.invalid_pswd_ids)
def test_elk_sign_up_invalid_password(browser, elk_open_sign_up_page, password):
    reg_page = RegPageHelper(browser)
    reg_page.create_password(password)
    if password == "":
        reg_page.enter_first_name("Дмитрий")
        reg_page.enter_surname("Сливный")
        email = "sliva997@mail"
        reg_page.enter_email(email)
        reg_page.click_on_register_button()
        assert "Длина пароля должна быть не менее 8 символов" in reg_page.check_input()
    else:
        reg_page.click_on_confirm_password()
        if password == TestDataSet.invalid_pswd[1]:
            assert reg_page.check_input() == "Длина пароля должна быть не менее 8 символов"
        elif password in [TestDataSet.invalid_pswd[2], TestDataSet.invalid_pswd[4]]:
            assert reg_page.check_input() == "Пароль должен содержать хотя бы одну заглавную букву"
        elif password == TestDataSet.invalid_pswd[3]:
            assert reg_page.check_input() == "Пароль должен содержать хотя бы одну прописную букву"
        elif password == TestDataSet.invalid_pswd[5]:
            assert reg_page.check_input() == "Пароль должен содержать только латинские буквы"
        elif password == TestDataSet.invalid_pswd[6]:
            assert reg_page.check_input() == "Длина пароля должна быть не более 20 символов"
        else:
            assert reg_page.check_input() != ""


@pytest.mark.parametrize("pswd2", ["", "399R8gSliva"], ids=["empty string", "mismatching password"])
def test_elk_unconfirmed_password(browser, elk_open_sign_up_page, pswd2):
    reg_page = RegPageHelper(browser)
    reg_page.enter_first_name("Дмитрий")
    reg_page.enter_surname("Сливный")
    email = "sliva997@mail"
    reg_page.enter_email(email)
    reg_page.create_password("399R8gSlivA")
    reg_page.confirm_password(pswd2)
    reg_page.click_on_register_button()
    if pswd2 == "":
        assert reg_page.check_input() == "Длина пароля должна быть не менее 8 символов"
    else:
        assert reg_page.check_input() == "Пароли не совпадают"

@pytest.mark.parametrize("region", [0, 1, 10, 70])
def test_elk_sign_up_diverse_regions(browser, elk_open_sign_up_page, region):
    reg_page = RegPageHelper(browser)
    reg_page.enter_first_name("Дмитрий")
    reg_page.enter_surname("Сливный")
    reg_page.select_region(region)
    email = "sliva997@mail.ru"
    reg_page.enter_email(email)
    reg_page.create_password("399R8gSliva")
    reg_page.confirm_password("399R8gSliva")
    reg_page.click_on_register_button()
    assert "Kод подтверждения отправлен на адрес" and email in reg_page.check_confirmation()