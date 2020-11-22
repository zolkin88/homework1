from page_objects.MainPage import MainPage
from page_objects.LoginPage import LoginPage
from page_objects.ProfilePage import ProfilePage
from page_objects.CategoryPage import CategoryPage
from page_objects.SamsungPage import SamsungPage
from page_objects.RegisterAccount import RegisterAccount
import allure


def test_main_page(browser):
    with allure.step(u'Открываем главную страницу Ozone.ru'):
        main_page = MainPage(browser)
    with allure.step(u'Проверям, что заголовок равен: ' + MainPage.TITLE):
        main_page.check_title()


def test_login_on_main_page(browser):
    with allure.step(u'Открываем главную страницу Ozone.ru'):
        main_page = MainPage(browser)
    with allure.step(u'Наживаем на кнопку "Войти"'):
        main_page.open_registration_form()
    with allure.step(u'Проверям, что открылась экранная форма регистрации'):
        pass

# def test_categories_number(browser):
#     categories_page = CategoryPage(browser)
#     assert 10 == categories_page.check_number_of_categories()
#     assert u'Desktops (13)' == categories_page.check_first_category_name()
#
#
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
