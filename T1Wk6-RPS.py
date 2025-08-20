# a = -11
# print(a % 2)  # any remainders left afterwards
# print(a // 2) # how many times it goes in completely

# def odd_checker(number):
#     if (number % 2) == 0:
#         print(f"{number} is even")
#         return True
#     else:return True
#         print(f"{number} is odd")
#         return False
#     
# userNum = int(input("Gimme a number: "))
# if odd_checker(userNum):
#     print("Good number!!")


#### Rock Paper Scissors
import random

def rps():
    options = ["Rock", "Paper", "Scissors"]
    print("Choose your weapon: ")
    print("0 = Rock, 1 = Paper, 2 = Scissors")
    
    ## player input
    player = int(input("I choose: "))
    
    # computer random option
    computer = random.randint(0,2)
    
    ### Show choices
    print(f"\nYou chose {options[player]}")
    print(f"Computer chose {options[computer]}")
    
    result = (player - computer + 3) % 3
    if result == 0:
        print("It's a tie!!")
    elif result == 1:
        print("Human wins!!")
    else:
        print("Computer wins!!")
    
rps()
    

