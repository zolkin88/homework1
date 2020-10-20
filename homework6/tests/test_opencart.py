from page_objects.MainPage import MainPage
from page_objects.LoginPage import LoginPage
from page_objects.ProfilePage import ProfilePage
from page_objects.CategoryPage import CategoryPage
from page_objects.SamsungPage import SamsungPage
from page_objects.RegisterAccount import RegisterAccount
import pytest
import allure


def test_main_page(browser, get_path, create_logger):
    logger = create_logger
    logger.info(u'Проверяем path')
    if get_path != "":
        pytest.skip(u'В параметрых передан не тот path')
    logger.info('Открываем главную страницу Opencart')
    main_page = MainPage(browser)
    logger.info('Проверяем заголов страницы')
    main_page.check_title()


def test_categories_number(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/index.php?route=product/category&path=20":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Откываем главную страницу категроий товаров'):
        categories_page = CategoryPage(browser)
    with allure.step(u'Проверям, что на данной странице отображены 10 товаров'):
        assert 10 == categories_page.check_number_of_categories()
    with allure.step(u'Проверям текст первой категории'):
        assert u'Desktops (13)' == categories_page.check_first_category_name()


def test_samsung_card(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/index.php?route=product/product&path=57&product_id=49":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Откываем стриничку с телефоном Самсунг'):
        samsung_page = SamsungPage(browser)
    with allure.step(u'Проверям, что это действительно страница Самсунг'):
        assert samsung_page.is_samsung_title() is True


def test_registration_account_page(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/index.php?route=account/login":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Откываем стриничку регистрации акаунта'):
        account_page = RegisterAccount(browser)
    with allure.step(u'Проверям, что это действительно страница регистрации'):
        assert account_page.is_it_registration_page() is True


def test_admin_page(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/admin":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Откываем страничку входа администратора'):
        login_page = LoginPage(browser)
    with allure.step(u'Проверям, что это действительно страница входа администратора'):
        assert login_page.is_admin_page() is True


def test_login_user(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/admin":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Открываем страницу регистрации'):
        login_page = LoginPage(browser)
    with allure.step(u'Вводим логин и пароль и нажимаем "Login"'):
        login_page.login_user('user', 'bitnami1')
    with allure.step(u'Открывается страница профиля'):
        profile_page = ProfilePage(browser)
    with allure.step(u'Проверяем имя профиля'):
        assert profile_page.check_user_name() == u'John Doe'


def test_log_out(browser, get_path):
    with allure.step(u'Проверям какой path передан'):
        if get_path != "/admin":
            pytest.skip(u'В параметрых передан не тот path')
    with allure.step(u'Открываем страницу регистрации'):
        login_page = LoginPage(browser)
    with allure.step(u'Вводим логин и пароль и нажимаем "Login"'):
        login_page.login_user('user', 'bitnami1')
    with allure.step(u'Открывается страница профиля'):
        profile_page = ProfilePage(browser)
    with allure.step(u'Проверям имя профиля'):
        assert profile_page.check_user_name() == u'John Doe'
    with allure.step(u'Выходим из профиля'):
        profile_page.log_out()
    with allure.step(u'Проверям, что мы снова на странице регистрации'):
        assert login_page.is_admin_page() is True
