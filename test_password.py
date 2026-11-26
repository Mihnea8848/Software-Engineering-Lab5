from password import check_password


def test_short_password():
    assert check_password("abc") == False


def test_long_password():
    assert check_password("abcdefghijk1") == True


def test_password_needs_digit():
    assert check_password("a" * 10) == False
    assert check_password("a" * 9 + "1") == True
