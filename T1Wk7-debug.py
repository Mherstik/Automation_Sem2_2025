x = 5
y = input("Gimme a number: ")

#z = int(z)
#print(type(z))
try:
    y = int(y)
    z = x/y
    print(type(z))
    print(z)
    print("Division = ", round(z,2))
except ZeroDivisionError:
    print("You tried to divide by zero. \nWho do you think you are?")
except ValueError:
    print("Take a look at yourself")
#except:
#    print('Something went wrong!')


c = 12
if c == 12:
    print("Assignment")
else:
    print("No assignment")

#### Assertion test


a = "Hello"
assert a == "Hello" , "Tell them what went wrong"
b = "Something"
assert b == "Something", "Now it's hello"



