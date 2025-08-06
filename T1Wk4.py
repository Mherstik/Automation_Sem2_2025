# Ask their name.
# Asks the user to enter their age.
# Stores the age in a variable.
# Uses an if statement to classify the user into different age groups:
#    If the user is 0 to 12 years old, print "You're a child."
#    If the user is 13 to 17 years old, print "You're a teenager."
#    If the user is 18 to 64 years old, print "You're an adult."
#    If the user is 65 years or older, print "You're a senior."
#Ensure only valid inputs are allowed.
#    - must be a number
#    - 0 to 125
#    - only 3 attempts

name = input("What is your name: ")
# age = input("Hello", name + ". What is your age: ") 
# ^^^^^ error because expected 1 argument and got 2

## validation attempts
# def validattempts(attempt):
#     global attempts
#     if attempt > 0 :
#         attempts = attempt -1
#         return attempts
#     else:
#         print("Out of attempts")
#         quit()

# test is is a number
# def numbercheck(num, attempts):
#     # validattempts(attempting)
#     for attempt in range(attempts)
#         if not num.isdigit():
#             print("Not a valid number")
#             return False, attempts
#         else:
#             print("Valid number")
#
# def numbercheck(num):
#     num = str(num)
#     # Handle empty string
#     if not num:
#         return False
#     # No sign present, just check if all characters are digits
#     return num.isdigit()
# 
# attempts = ''
# ### Get users age
# def getage():
#     global attempts
#     attempts = 3
#     age = input(f"Hello {name}. What is your age: ")
#     if attempts > 0:
#         print(attempts)
#         numbercheck(age)
#         age = input("Try again: ")
#         attempts = attempts - 1
# 
# 
#             
# getage()
# 
# def getchuppas():
#     attempting = 3
#     chuppas = input("How many chuppa chupps do you have: ")
#     numbercheck(chuppas, attempting)
# 
# getchuppas()
# def getlollies():
#     attempts = 3
#     lollies = input("How many lollies are left: ")
#     numbercheck(lollies)

## Attempt 2
# Introduce Try/Except
# Get age and only give them three attempts

print(f"Hello {name}. What is your age", end="")
def num_test(user_num):
    try:
        float(user_num)
        print("Your number is valid")
        return True
    except ValueError:
        print("Your number is invalid")
        return False
    except:
        print("Something else went wrong!")
        return False

def validator(prompt=": "):
    user_num = input(prompt)
    attempts = 3
    # while attempts in range(3):
    while 0 < attempts <= 3:
        attempts = attempts - 1
        if attempts == 0:
            print("Too many attempts!\nTake a look at yourself!")
            break
        elif num_test(user_num):
            #quit()
            break
        else:
            user_num = input("Give me a valid number: ")
    
    
validator()
print("Made it to here!!")

print("How many cookies are left?", end='')
validator()
