
description = 'Test for checking navigating via main menu'

pages = ['header.menu']

def setup(data):
    pass

def test(data):
    navigate('http://www.simplesite.com/?culturekey=en')
    click(header.menu.CS)
    verify_text('FAQ')
    click(header.menu.Features)
    verify_text('Your website')
    click(header.menu.Theam)
    click(header.menu.Login_button)
    verify_text('USERNAME, EMAIL OR DOMAIN NAME')
    # http_get('http://google.com/')
    # assert_equals(data.last_response.status_code, 200)

def teardown(data):
    pass
