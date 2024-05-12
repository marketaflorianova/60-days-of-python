password = input("Enter new password: ")

result = []
if len(password) >=8:
    result.append(True)
else:
    result.append(False)

digit = False
for char in password:
    if char.isdigit(): # if the password doesn't contain a number, the following line won't get executed and the `digit` variable won't be overwritten
        digit = True
result.append(digit)

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True
result.append(uppercase)

print(all(result)) # returns False if at least one is False


if all(result):
    print("Strong password")
else:
    print("Weak password")