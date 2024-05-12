def check_strength_password(password):
    result = []
    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    digit = False
    for char in password:
        if char.isdigit():  # if the password doesn't contain a number, the following line won't get executed and the `digit` variable won't be overwritten
            digit = True
    result.append(digit)

    uppercase = False
    for char in password:
        if char.isupper():
            uppercase = True
    result.append(uppercase)

    if all(result):
        message = "Strong Password"
    else:
        message = "Weak Password"

    return print(message)

check_strength_password("hello")