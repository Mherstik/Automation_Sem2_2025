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
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    print("\nChoose your weapon: ")
    # print("0 = Rock, 1 = Paper, 2 = Scissors, 3 = Lizard , 4 = Spock")
    for i in range(len(options)):
        print(f"{i} = {options[i]}")
            
    
    ## player input
    player = int(input("I choose: "))
    
    # computer random option
    computer = random.randint(0, len(options) - 1 )
    
    ### Show choices
    print(f"\nYou chose {options[player]}")
    print(f"Computer chose {options[computer]}")
    
    result = (player - computer + len(options)) % len(options)
    if result == 0:
        #print("It's a tie!!")
        return 0
    elif result == 1:
        #print("Human wins!!")
        return 1
    else:
        #print("Computer wins!!")
        return -1

## Best of 3
games = 3
wins = 0
while games > 0:
    wins += rps()  # wins = wins + rps()
    games -=1
if wins == 0:
    print("You tied")
elif wins >= 1:
    print("Human wins")
else:
    print("Computer wins")
    

