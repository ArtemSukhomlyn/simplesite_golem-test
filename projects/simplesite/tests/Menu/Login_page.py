
description = 'Checking login page'

pages = ['header.menu',
         'Login_page']

def setup(data):
    pass

def test(data):
    navigate('http://www.simplesite.com/?culturekey=en')
    click(header.menu.Login_button)
    send_keys(Login_page.username_login_field, 'test_user')
    send_keys(Login_page.password_login_field, 'test_password')
    click(Login_page.Login_buttom)
    wait(3)
    verify_exists(Login_page.Login_error_text)

def teardown(data):
    pass
