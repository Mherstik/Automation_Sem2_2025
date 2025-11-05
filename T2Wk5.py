### Get info from user
# Name
# Age
# Postcode
# Check to see if in file
import csv
import time

name = input("What is your name: ")
age = input("What is your age: ")
postcode = input("What is your postcode: ")
timestamp = time.localtime()

formatted_time = time.strftime('%Y-%m-%d %H:%M', timestamp)
# ChatGPT/AI link here??

print(name, age, postcode, formatted_time)
print(name +','+ age +','+ postcode +','+ formatted_time)

filename = 'peepdeets.csv'
def addPerson():
    newPerson = [name, age, postcode, formatted_time]
    with open(filename, mode='a') as csvfile:
        csvW = csv.writer(csvfile)
        csvW.writerow(newPerson)
        csvfile.close()

addPerson()
