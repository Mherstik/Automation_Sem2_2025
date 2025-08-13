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

for attempt in range(1, MAX_ATTEMPTS + 1):    
    pword = input(f"{name}, give me a password: ")
    if len(pword) >= 10:
        print("Password meets minimum length")
        break
    else:
        print("Password DOES NOT meet minimum length")
        if attempt == MAX_ATTEMPTS:
            print("Maximum attempts reached. Access denied!")
        else:
            print(f"{name} you have {MAX_ATTEMPTS - attempt} attempts left")
    
for char in pword:
    if char.isupper():
        pass
    else:
        print(f"{char} is not an upper character")
        
    
    
    