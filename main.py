# input password
password = input("please enter a new password: ")

# check which of the rules are true to confirm password strength
validity = {}

# check if password length is long
if len(password) >= 8:
    validity["length"] = True
else:
    validity["length"] = False

# check if password has a number
has_digit = False
for i in password:
    if i.isdigit():
        has_digit = True
validity["digit"] = has_digit

has_uppercase = False
for i in password:
    if i.isupper():
        has_uppercase = True
validity["upper-case"] = has_uppercase

if all(validity.values()):
    strength = "strong"
else:
    strength = "weak"

print(strength + " password")