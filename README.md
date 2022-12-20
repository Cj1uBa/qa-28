Проект по тестированию сервиса Ростелеком согласно их ТЗ

test_data.py хранит наборы с тестовыми значениями
сonftest.py содержит фикстуры для открытия веб-страниц

reg_tests.py тесты на страницы регистрации:
auth_tests.py Тесты на страницы авторизации:
recovery_tests.py тесты на страницы востановления пароля:
get_code_tests.py Тестф на страницы авторизации по временному коду:


Список тестов
1.	test_elk_default_tab Проверка что по умолчанию выбран ввод телефона
2.	test_elk_switch_to_email_tab Автоматическое переключение на почту
3.	test_elk_switch_to_login_tab Автоматическое переключение на логин
4.	test_elk_switch_to_phone_tab Автоматичекое переключени на телефон
5.	test_elk_phone_authorization_no_such_user Вход по не валидным данным
6.	test_elk_invalid_username_authorization Ввод невалидного логина пользователя
7.	test_elk_invalid_password_authorization Ввод не валидного пароля
8.	test_key_web_invalid_one_time_code Авторизация не валидным временным кодом
9.	test_key_web_go_to_pswd_auth_page Переход со страницы авторизации по коду на обычную страницу авторизации
10.	test_key_web_return_to_one_time_code Переход со страницы авторизации на страницу авторизации по временному коду(возврат)
11.	test_onlime_get_one_time_code_by_email Отправка временного кода на почту
12.	test_smarthome_get_code_positive Отправка временного кода по телефону
13.	test_start_web_invalid_phone_or_email Ввод не валидного номера телефона или почты на странице входа по коду
14.	test_elk_pswd_recovery_captcha Востановление с не валидной капчей
15.	test_elk_sign_up_diverse_regions Отправка формы регистрации с разных регионов. Данные валиды
16.	test_elk_sign_up_invalid_first_name Ввод имени в невалидном формате
17.	test_elk_sign_up_invalid_surname Ввод фамилии в невалидном формате
18.	test_elk_sign_up_invalid_phone_or_email Ввод телефона (почты) в невалидном формате
19.	test_elk_sign_up_invalid_password Создание не валидного пароля
20.	test_elk_unconfirmed_password Отправка формы с не совпадающими паролями
