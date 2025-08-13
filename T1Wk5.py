
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.printable)
print("punctuation", string.punctuation)

special_char = "!@#$%^&*()_+-=<>?:{}|[]\,./'" + '"'
name = input("Give me a name: ")
print(len(name))

# Check to make sure the password has at least 10 characters
# User has 3 attempts to put a valid password
# Bonus - must have at least 1 uppercase, 1 lowercase & 1 number
# Bonus Bonus - and 1 special character
# print(name.upper())
# print(name.lower())
# for each in name:
#     print(each)

MAX_ATTEMPTS = 3
MIN_LENGTH = 16

def get_password():
    pass

    
def upper_test(pword):
    for char in pword:
        if char.isupper():
            return True
        else:
            continue
    return False

def lower_test(pword):
    for char in pword:
        if char.islower():
            return True
        else:
            continue
    return False

def is_number(pword):
    for char in pword:
        if char.isdigit():
            return True
        else:
            continue
    return False

for attempt in range(1, MAX_ATTEMPTS + 1):    
    pword = input(f"{name}, give me a password: ")
    if len(pword) >= MIN_LENGTH:
        print("Password meets minimum length")
        if upper_test(pword) and lower_test(pword):
            print("It meets upper and lower")
            if is_number(pword):
                print("It has a number")
                break
            else:
                print("Password needs a number too!")
                continue
        elif upper_test(pword):
            print("Password has upper")
            print("Needs a lower")
            continue
        elif lower_test(pword):
            print("Password has lower")
            print("Needs an upper")
            continue
        else:
            print("Password has NO upper or lower")
            continue
        # break
    else:
        print("Password DOES NOT meet minimum length")
        if attempt == MAX_ATTEMPTS:
            print("Maximum attempts reached. Access denied!")
        else:
            print(f"{name} you have {MAX_ATTEMPTS - attempt} attempts left")

