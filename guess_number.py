import random

def game():

    # introduction
    print('''
Welcome ... 
Are you ready to guess THE NUMBER??? (insert: "1")
Or do you want to CHALLENGE the computer to guess your number? (insert: "2")''')
    
        # implement flow writing
        # input 
    playstyle = int(input('-> '))

    # set difficulty 

    # playstlye 1
    # random number in a certain range
    # boarders can be defined through difficulty level 
    
    difficulty = None

    while difficulty == None:
      difficulty = int(input('''
Please insert the level of difficulty: 
  Easy: "1"
  Medium: "2"
  Hard: "3"
  -> '''))
      
      x = None
      y = None

      if difficulty == 1: 
        x = -10 
        y = 10   
      elif difficulty == 2:
        x = -1000
        y = 1000 
      elif difficulty == 3:
        x = -1000000
        y = 1000000
      else:
        print('Your input was invalid. Please try again!')
        difficulty = None 

    print(f'The searched number is between {x} and {y} including these numbers.')

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
          print(f'Your guess was right. The searched number was "{searched_number}"!')
        else:
          print('Your guess was invalid. Please try again!')
    # playstyle 2 
game()
