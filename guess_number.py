import random
import time
import sys

def game():


  introduction ='''
Welcome ... 
Choose your playstle ...
  User guesses: "1"
  Computer guesses: "2"\n'''

  # __init__ modul for not repeating code all the time?
  for char in introduction:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

        # input 
  playstyle = int(input('Input: '))

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

  print(f'The searched number is between "{x}" and "{y}" including these numbers.')

    # start timer 
  start_time = time.time()


  searched_number = random.randint(x, y)
    # while loop that keeps answers the user to the guess
    
  guess = None 

  while True:
      try: 
        while guess != searched_number:
          guess = int(input('Insert your guess: '))
          if guess < searched_number:
            print('Your guess was too low.')
          elif guess > searched_number:
            print('Your guess was too high.')

        break  

      except ValueError:
        print('Your guess was invalid. Please try again!')

    # while guess != searched_number:
    #     if guess < searched_number:
    #       print('Your guess was too low.')
    #     elif guess > searched_number:
    #       print('Your guess was too high.')  
    #     else:
    #       print('Your guess was invalid. Please try again!')

        
  end_time = time.time()
  elapsed_time = end_time - start_time
  rounded_time = round(elapsed_time, 2)
  print(f'Your guess was right. The searched number was "{searched_number}"!\nTime record: {rounded_time} s')

    # playstyle 2 
game()
