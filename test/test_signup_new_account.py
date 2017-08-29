import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    username = random_string("user", 10)
    password = "test"
    email =  "%s@localhost" % username
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
#    assert app.session.is_logged_in_as(username)
    assert app.soap.can_login(username, password)
