def check_password(pw):
    return len(pw) >= 10 or any(c.isdigit() for c in pw)
