import random

lt = ["Rock" , "Paper" , "Scissors"]

def getChoices():

    playerChoice = input("Enter a choice (RPS): ")

    computerChoice = random.choice(lt)
    
##Random library 'choice' is choosing randomly from the list
    choices = {"player" : playerChoice, "computer": computerChoice}

    return choices

choices = getChoices()
##print(choices)

def checkWin(player, computer):
    print(f"Your chose {player} and computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    
    elif player == "Rock":
        if computer == "Paper":
            return "Computer wins!"
        elif computer == lt[2]:
            return "PLayer wins"
        
    elif player == "Paper":
        if computer == "Rock":
            return "Player wins!"
        elif computer == lt[2]:
            return "Computer wins"
        
    elif player == lt[2]:
        if computer == "Paper":
            return "Player wins!"
        elif computer == "Rock":
            return "Computer wins"
    else:
        return "Type Rock , Paper , Scissors... to get the result."

'''
instead of this you can do this ^

    elif player ==lt[0] and computer == lt[1]:
        return "Computer is the winner!"

    elif player ==lt[1] and computer == lt[2]:
        return "Computer is the winner!"
    
    elif player ==lt[0] and computer == lt[2]:
        return "You are the winner!"

    elif player ==lt[1] and computer == lt[0]:
        return "You are the winner!"

    elif player ==lt[2] and computer == lt[1]:
        return "You are the winner!"

    elif player ==lt[2] and computer == lt[0]:
        return "Computer is the winner!"

'''          

Result = checkWin(choices["player"], choices["computer"])

print(Result)

'''
def greeting():
    return "Hi"
##when you return a function as a string it won;t get printed
print(greeting())
'''


'''
##Dictionary
dict = {"name" : "beau", "color" : choices}
print(dict["name"])

'''

'''
##if,elif,else

age = 20

if age>=18:
    print("youre an adult")

elif age>=12:
    print("youre a teen")

else:
    print("youre a kid")
##once one of the conditions is true it wont check other
'''
