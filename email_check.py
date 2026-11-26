def is_valid_email(s):
    print("checking", s)
    return "@" in s and "." in s and " " in s
