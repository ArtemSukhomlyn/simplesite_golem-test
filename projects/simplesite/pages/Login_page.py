

FB_login_button = ('id', '_ctl0_facebookControl_lblStatus', 'FB_login_button')

Login_buttom = ('id', 'loginBox_loginbtn', 'Login_buttom')

Login_error_text = ('xpath', '/html/body/form/div[5]/div[1]/div/div/div/div[2]/span', 'Login_error_text')

forgot_password_link = ('css', 'loginBox_forgotpw', 'forgot_password_link')

forgot_user_link = ('css', 'loginBox_forgotusr', 'forgot_user_link')

password_login_field = ('id', 'loginBox_password', 'password_login_field')

username_login_field = ('id', 'loginBox_username', 'username_login_field')


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
    verify_text_in_element(Login_page.Login_error_text, 'It looks like you')


def setup(data):
    pass
