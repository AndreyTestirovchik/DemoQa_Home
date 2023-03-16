from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs.exist_icon()


def test_user_name_exist(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs.find_element('#user-name')


def test_password_exist(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs.find_element('#password')
