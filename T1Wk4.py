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
# ^^^^^ error because expected 1 argument and got 2.

age = input(f"Hello {name}. What is your age: ")

# test is is a number
def numbercheck(num):
    if not num.isdigit():
        print("Not a valid number")
        return False
    else:
        print("Valid number")

numbercheck(age)

chuppas = input("How many chuppa chupps do you have: ")
numbercheck(chuppas)

lollies = input("How many lollies are left: ")
numbercheck(lollies)
