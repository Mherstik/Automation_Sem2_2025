####
# STORE THE PASSWORD IN A FILE
###
# READ THE PASSWORD AND MAKE SURE IT'S NOT THE SAME
# If  the same - tell them it's the same
# BONUS - put it in again


# password = input("Gimme yo passwd bro: ")


f1 = "filename.txt"
## READ THE FILE
f = open(f1, "r")
filecontents = f.read()
# print(type(filecontents))
print(filecontents)
f.close()

## Write to the file
f = open(f1, 'w')
f.write("New content to write")
f.close()

## READ THE FILE AGAIN
print("READING FILE")
f = open("filename.txt", "r")
print(f.read())