# Input: marks

marks = input("What was your score: ")

# print(type(marks))
marks = float(marks)  # Convert to integer ??
# print(type(marks))

# Output: letter grade or message (print)
# if (marks > 100)
if marks > 100:
    print("Out of range")
#   print Out of range 0-100
# else if (marks > 84)
elif marks > 84:
    print("HD")
#   print HD
# else if (marks > 74) 
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


