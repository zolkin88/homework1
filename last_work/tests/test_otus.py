from page_objects.MainPage import MainPage
from page_objects.LoginPage import LoginPage
from page_objects.ProfilePage import ProfilePage
from page_objects.CategoryPage import CategoryPage
from page_objects.SamsungPage import SamsungPage
from page_objects.RegisterAccount import RegisterAccount
from page_objects.CoursesPage import CoursesPage
from page_objects.PythonQaPage import PythonQaPage

import allure


def test_main_page(browser):
    with allure.step(u'Открываем главную страницу Ozone.ru'):
        main_page = MainPage(browser)
    with allure.step(u'Проверям, что заголовок равен: ' + MainPage.TITLE):
        main_page.check_title()


# def test_login_on_main_page(browser):
#     with allure.step(u'Открываем главную страницу Ozone.ru'):
#         main_page = MainPage(browser)
#     with allure.step(u'Наживаем на кнопку "Вход или регистрация"'):
#         main_page.open_registration_form()
#     with allure.step(u'Вводим логин'):
#         main_page.input_email(u'dzolkin@htsts.ru')
#     with allure.step(u'Вводим пароль'):
#         main_page.input_email(u'Zol7013340')
#     with allure.step(u'Жмем кнопку Войти'):
#         main_page.click_submit_button()
#     with allure.step(u'Проверям, что попали в личный кабинет'):
#         user_page = UserPage(browser)
#         assert user_page.check_user_name() == u'Дмитрий Золкин'

def test_check_numbers_of_courses(browser):
    main_page = MainPage(browser)
    with allure.step(u'Проверяем, что в списке курсов есть: Тестирование'):
        main_page.check_testing_course()
    with allure.step(u'Проверяем, что на странице курсов по тестированию 12 курсов'):
        courses_page = CoursesPage(browser)
        numbers = courses_page.get_number_of_courses()
        # allure.attach("Ожидаемый результат:12",)
        assert numbers == 12

#
# def test_python_qa_engineer_in_list(browser):
#     main_page = MainPage(browser)
#     with allure.step(u'Проверяем, что в списке курсов есть: Тестирование'):
#         main_page.check_testing_course()
#         courses_page = CoursesPage(browser)
#     with allure.step(u'Получаем названия всех курсов'):
#         names = courses_page.get_names_of_courses()
#     with allure.step(u'Проверяем, что в этом списке есть курс "Python QA Engineer"'):
#         assert "Python QA Engineer" in names


# def test_check_nearest_courses_python_qa_engineer(browser):
#     nearest_date = '21 декабря'
#     main_page = MainPage(browser)
#     with allure.step(u'Проверяем, что в списке курсов есть: Тестирование'):
#         main_page.check_testing_course()
#         courses_page = CoursesPage(browser)
#     with allure.step(u'Переходим на страницу курса Python QA'):
#         courses_page.go_to_python_qa()
#     with allure.step(u'Проверяем ближайшую дату начала занятий'):
#         python_qa_page = PythonQaPage(browser)
#         allure.attach('',
#                       'Ожидаемый результат: {0}, Полученный результат: {1}'.format(nearest_date,
#                                                                                    python_qa_page.get_nearest_courses_date()),
#                       allure.attachment_type.TEXT)
#         assert nearest_date == python_qa_page.get_nearest_courses_date()

        # def test_python_qa_engineer_start_in_next_year()
        # def test_samsung_card(browser):
        #     samsung_page = SamsungPage(browser)
        #     assert samsung_page.is_samsung_title() is True
        #
        #
        # def test_registration_account_page(browser):
        #     account_page = RegisterAccount(browser)
        #     assert account_page.is_it_registration_page() is True
        #
        #
        # def test_admin_page(browser):
        #     login_page = LoginPage(browser)
        #     assert login_page.is_admin_page() is True
        #
        #
        # def test_login_user(browser):
        #     login_page = LoginPage(browser)
        #     login_page.login_user('user', 'bitnami1')
        #     profile_page = ProfilePage(browser)
        #     assert profile_page.check_user_name() == u'John Doe'
        #
        #
        # def test_log_out(browser):
        #     login_page = LoginPage(browser)
        #     login_page.login_user('user', 'bitnami1')
        #     profile_page = ProfilePage(browser)
        #     assert profile_page.check_user_name() == u'John Doe'
        #     profile_page.log_out()
        #     assert login_page.is_admin_page() is True
