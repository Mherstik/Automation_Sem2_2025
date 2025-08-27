###
# Convert Fahrenheit to Celcius
###
# C = (F - 32) × 5/9

def getUserTemp():
    userDegree = input("What is the temperature: ")

    while True:
        try:
            userDegree = int(userDegree)
            return userDegree
            break
        except:
            print("Please put a valid number.")
            userDegree = input("What is the temperature: ")

# userTemp = getUserTemp() # Move to the bottom

def convertFtoC(userTemp):
    # C = (F - 32) × 5/9
    celcius = (userTemp - 32) * 5 / 9
    # celcius = round(celcius,2)
    # celcius = round(((userTemp - 32) * 5 / 9),2)
    print(f"{userTemp}F is equal to {celcius:.2f}C")

def convertCtoF(userTemp):
    # F = (C * 9/5) + 32
    fahrenheit = (userTemp * 9/5) + 32
    print(f"{userTemp}C is equal to {fahrenheit:.2f}F")


###
## Ask the user what they want to convert to or from
###
print("What do you want to do?\n1-Convert Fahrenheit to Celcius\n2-Convert Celcius to Fahrenheit")
##
userChoice = input("Option: ")
userTemp = getUserTemp()
if userChoice == "1":
    convertFtoC(userTemp)
elif userChoice == "2":
    convertCtoF(userTemp)
elif userChoice == "3":
    convertFtoC(userTemp)
    convertCtoF(userTemp)
else:
    print("Invalid choice")

