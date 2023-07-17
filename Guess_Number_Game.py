"""Module providingFunction for selecting rendom object. This is number guess game when your guess then between 1 to 10 
and the process till continue for corect guess or 3 incorect guess 
"""
import random
# print (Rnumber)

#user Registration 
gammer_name = input('Please Enter the player Name: >>>> ')
Welcome__note = print(f'--------WELCOME TO GUESS NUMBER GAME {gammer_name}------------- \n <><><><><><><><><><><> GAME START NOW <><><><><><><><>')
#game close function 

def gameclose():
    useranswar=input('Do you want to play again or quit this game? Ans-y/n:\n Please In').lower()
    if useranswar == 'y':
        print('New Game Start............')
        return True
    else:
        return False
# main game function 
def maingame(score,count):
    Rnumber = random.randint(1,10)
    # print(Rnumber)
    user_guessnum = int(input('Please Guess a Number between 1 to  10 :\n Enter Number : >>>> '))
    if user_guessnum == Rnumber:
        print(f'Congratulation {gammer_name} you Guess the Correct number: which is {user_guessnum}')
        if gameclose() == True:
            maingame(score+1,0)
        else:
            print(f'Your Score Is ::{score}')
            print(f'Thank you for playing this game {gammer_name}')

    else:
        print('your guess is incorect Please try Again')

        if count<3:
            print(f'your remaining {3-count} chance')
            maingame(score,count+1)
        else:
            print('>>>>>>> Game Over Your reach the Limit <<<<<<<  \n :::::: Thank You For playing this Game ::::::: ')
            print(f'The Random number is {Rnumber}')

            exit()

maingame(1,0)        
