def is_simple_valid_password(password):

    if password.count('@') != 1:
        return False

    local, domain = password.split('@')

    if not local or not domain:
        return False

    if '.' not in domain:
        return False

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.")

    for char in password:
        if char not in allowed_chars:
            return False

    return True

password = input("Enter an password address to validate: ")
if is_simple_valid_password(password):
    print("Valid password")
else:
    print("contains space.")
