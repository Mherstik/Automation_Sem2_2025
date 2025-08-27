###
# Convert Fahrenheit to Celcius
###
# C = (F - 32) × 5/9

def getUserTemp():
    userDegree = input("What is the temperature in F: ")

    while True:
        try:
            userDegree = int(userDegree)
            return userDegree
            break
        except:
            print("Please put a valid number.")
            userDegree = input("What is the temperature in F: ")

userTemp = getUserTemp()

def convertFtoC(userTemp):
    # C = (F - 32) × 5/9
    celcius = (userTemp - 32) * 5 / 9
    # celcius = round(celcius,2)
    # celcius = round(((userTemp - 32) * 5 / 9),2)
    print(f"{userTemp}F is equal to {celcius:.2f}C")

def convertCtoF(userTemp):
    # F = (C * 9/5) + 32
    pass

###
## Ask the user what they want to convert to or from
###
convertFtoC(userTemp)
