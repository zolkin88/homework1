from page_objects import MainPage


# def test_check_title(browser):
#     MainPage(browser).check_title()


def test_login(browser):
    MainPage(browser).login_user()

# def test_add_to_wish_list(browser):
#     product_name = MainPage(browser).get_featured_product_name(1)
#     MainPage(browser) \
#         .click_featured_product(1) \
#         .add_to_wishlist() \
#         .alert.click_login()
#     UserPage(browser) \
#         .login_user(email="test2@mail.ru", password="tests") \
#         .open_wishlist() \
#         .verify_product(product_name)
#
#
# def test_add_to_cart(browser):
#     product_name = MainPage(browser).get_featured_product_name(1)
#     MainPage(browser).click_featured_product(1)
#     ProductPage(browser) \
#         .add_to_cart() \
#         .alert.click_to_cart()
#     CartPage(browser) \
#         .verify_product(product_name) \
#         .checkout()
#     UserPage(browser) \
#         .login_user(email="test2@mail.ru", password="tests") \
#         .verify_payment_form()
