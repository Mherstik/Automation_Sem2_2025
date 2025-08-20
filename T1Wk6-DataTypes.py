### LISTS

option1 = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

options = ["Rock",
          "Paper",
          "Scissors",
          "Lizard",
          "Spock"]

print(options[0])
print(len(options))
player = "Spock"
if player in options:
    print("It's in there")
    
    
for each in options:
    print(each) #,end='')
    
### SETS
# Creating a set
fruits = {"apple", "banana", "cherry", "orange", "banana", "mango"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Creating a set from a list (duplicates removed)
numberlist = [3, 1, 2, 2, 4]
print(numberlist)
numbers = set([3, 1, 2, 2, 4])
print(numbers)  # Output: {1, 2, 3, 4}
    