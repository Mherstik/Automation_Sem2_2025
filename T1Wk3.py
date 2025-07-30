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
    if not user_input.isdigit():
        print("You didn't enter a number!")
        continue
    ## NEXT BLOCK
    marks = int(user_input)
    if marks < 0 or marks >= 100:
        print("Out of bounds")
        continue
    else:
        if marks > 84:
            print("HD")
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
    
    


