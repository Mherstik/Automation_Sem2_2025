### Get info from user
# Name
# Age
# Postcode
# Check to see if in file
import csv
import time

name = input("What is your name: ").lower()
age = input("What is your age: ")
postcode = input("What is your postcode: ")
timestamp = time.localtime()

formatted_time = time.strftime('%Y-%m-%d %H:%M', timestamp)
# ChatGPT/AI link here??

print(name, age, postcode, formatted_time)
print(name +','+ age +','+ postcode +','+ formatted_time)

filename = 'peepdeets.csv'

### Does file exist?
# if no, create file and add headers!

def addPerson():
    newPerson = [name, age, postcode, formatted_time]
    with open(filename, mode='a') as csvfile:
        csvW = csv.writer(csvfile)
        csvW.writerow(newPerson)
        csvfile.close()


def comparePerson():
    global need2write
    with open(filename, mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            #print(row)
            if name.capitalize() == row['Name'].capitalize() and age == row['Age']:
                print(f"{name} matches data in row!")
                exit()
            else:
                print(f"{name} doesn't match {row['Name']}. Moving on!")
                need2write = 'True'
        return need2write

comparePerson()   exit()

if need2write == 'True':
    addPerson()
