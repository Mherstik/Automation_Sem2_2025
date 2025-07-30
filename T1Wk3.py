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

while True:
    name = input("Give me a name: ")
    if name == "Marcus":
        print("You rock!")
        break
    else:
        print("Give me a better name!")

