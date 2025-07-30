## Count to 10

i = 0

## Get the number, check if it's less than 10
## If less than 10, add 1
## If not less than 10 - break
while i < 10:
    print(i)
    i = i + 1
    # i += 1
print("I'm here!")


somelist = [1,3,5,7,9]
for each in somelist:
    print(each)
    print("Get the next number...")
print("We're out")

# while True:
#     name = input("Give me a name: ")
#     if name == "Marcus":
#         print("You rock!")
#         break
#     else:
#         print("Give me a better name!")
#
### Loop until they give me a number!!

# user_input = int(input("Can I have your score please: "))

while True:
    user_input = input("Can I have your score please: ")
    ## FIRST BLOCK
    ## TEST - did they give a number?
    if not user_input.isdigit():
        print("You didn't enter a number!")
        continue
    ## NEXT BLOCK
    # Convert string (user_input) to integer and store as marks
    marks = int(user_input)
    # CHeck if it's out of bounds
    if marks < 0 or marks >= 100:
        print("Out of bounds")
        continue
    else:
        if marks > 84:
            print("A score of " + str(marks) + "is an HD")
        elif marks > 74:
            print("D")
        # else if (marks> 64)
        elif marks > 64:
            print("C")
        # else if (marks > 49)
        elif marks > 49:
            print("P")
        else:
            print("F")
        break
    # > greater than
    # >= greater than or equal to
    # < less than
    # <= less than or equal to
    # == is equal to
    # != not equal to
###
###
# TEMP Checker
# What is the temp??
# Ask the user to enter the temperature
temperature = int(input("Enter the current temperature in Celsius: "))

# Above 40C is DARN HOT!!
if temperature >= 40:
    print(f"{temperature}C makes it a DARN hot day!")
# Above 30C is hot
elif temperature >= 30:
    print(f"{temperature}C makes it a hot day!")
# 21-29 = nice!!
elif temperature >= 20:
    print(f"{temperature}C makes it a nice day!")
# 10 -20 = cold
elif temperature > 10:
    print(f"It's a bit cold today. It's {temperature}C.")
# below 10 = freezing!!
# else:
#     "It's FREEZING!"
    


