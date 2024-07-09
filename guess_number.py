import random

def game():

    # introduction
    print('''
Welcome ... 
Are you ready to guess THE NUMBER??? (type "1")
Or do you want to CHALLENGE the computer to guess your number? (type "2")
          ''')
    
        # implement flow writing
        # input 
    playstyle = int(input('-> '))

    # set difficulty 

    # playstlye 1
    # random number in a certain range
    # boarders can be defined through difficulty level 
    x = -10 
    y = 10 
    searched_number = random.randint(x, y)
    # while loop that keeps answers the user to the guess
    guess = None 
    while guess != searched_number:
        guess = int(input('Insert your guess: '))
        if guess < searched_number:
          print('Your guess was too low.')
        elif guess > searched_number:
          print('Your guess was too high.')
        elif guess == searched_number:
          print(f'Your guess was right. The searched number was {searched_number}!')
        else:
          print('Your guess was invalid. Please try again!')
    # playstyle 2 
game()
