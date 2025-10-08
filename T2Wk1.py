listA = ["car", "plane", "ship"]
listB = [11, 23, 7, 23, 3]
print(listA)
print(listB)
print(listB[3])

mytuple = ("car", "plane", "ship", "bus", "CLOWNS")
print(mytuple)
## print item 3
print(mytuple[3])

myset= {"car", "plane", "ship", "bus"}
print(myset)
# print(myset[3]) # Can't do a set because it't unordered


listA.append("motorcycle")
print(listA)
# mytuple.append("motorcycle") # can't append as it's immutable
print(mytuple)


mydict = {
    "name" : "Marcus",
    "age" : 48,
    "sex" : "M"
    #"name" : "Tom"
    }
print(mydict)

## print name only from dict
print(mydict["name"])

### Save the dictionary to a file
# 
with open("something.csv", "w") as file:
    file.write(str(mydict))

with open("something.csv","r") as file:
    contents = file.read()
    print(contents)

