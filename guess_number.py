import random
import time
import sys

def game():

  introduction ='''
Welcome to Guess Game ... 
Choose your playstle ...'''

  # __init__ modul for not repeating code all the time?
  for char in introduction:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

    if char in ".!?": # when the charater fits into the string
      time.sleep(0.5)

        # input 
  playstyle = int(input('''
- "1" for user guesses
- "2" for computer guesses 
'''))

    # set difficulty 

    # playstlye 1
    # random number in a certain range
    # boarders can be defined through difficulty level 

  if playstyle == 1: 

    difficulty = None

    while difficulty == None:
      asking_for_difficulty = '''
Please insert the level of difficulty ...'''
    
      for char in asking_for_difficulty:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

        if char in ".!?": # when the charater fits into the string
          time.sleep(0.5)
  
      difficulty = int(input('''  
- "1" for easy
- "2" for medium
- "3" for hard
'''))

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

    num_range_text = f'\nThe searched number is between "{x}" and "{y}" including these numbers ...\n'

    for char in num_range_text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.05)

      if char in ".!?": # when the charater fits into the string
        time.sleep(0.5)

    text_game_start = 'The game starts in ...\n'

    for char in text_game_start:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.05)

      if char in ".!?": # when the charater fits into the string
        time.sleep(0.5)

  # simple countdown
    print('5')
    time.sleep(1.0)
    print('4')
    time.sleep(1.0)
    print('3')
    time.sleep(1.0)
    print('2')
    time.sleep(1.0)
    print('1')
    time.sleep(1.0)
    print('Go!')
  
  # advanced countdown
    # for x in range(0,5): but the count should count down!
      # print(x)
      # time.sleep(1.0)  

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
