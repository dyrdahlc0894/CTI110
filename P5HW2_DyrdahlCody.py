# This program is a small guessing game using random generated numbers and checks user input against said numbers.
# 11/29/22
# CTI-110 P5HW2 - Math Quiz
# Cody Dyrdahl
#
import random
user_input = 0;
print('Welcome to Math Quiz')
def main_menu():
  print()
  print('MAIN MENU')
  print('----------------')
  print('1. Adding Random Numbers')
  print('2. Subtracting Random Numbers')
  print('3. Exit')
  print()
def add_random_num():
  random_1 = random.randint(0,10);
  random_2 = random.randint(0,10);
  result = random_1 + random_2
  return result
def subtract_random_num():
  random_1 = random.randint(0,10);
  random_2 = random.randint(0,10);
  result = random_1 - random_2;
  return result
while user_input != 3:
  main_menu()
  user_input = int(input('Enter your choice: '))
  if user_input == 1:
    result = add_random_num()
    num_guess = 0;
    while user_input != result:
      print()
      user_input = int(input('Enter your guess 0 - 20: '))
      num_guess = num_guess + 1;
      if user_input < result:
        print('Sorry guess is too low')
      elif user_input == result:
        print()
        print('Right on the Money!')
        print('Number of guesses: ', num_guess)
      else:
        print('Sorry guess is too high')
  elif user_input == 2:
    result = subtract_random_num()
    num_guess = 0;
    while user_input != result:
      print()
      user_input = int(input('Enter your guess 0 - (-10): '))
      num_guess = num_guess + 1;
      if user_input < result:
        print('Sorry guess is too low')
      elif user_input == result:
        print()
        print('Right on the Money!')
        print('Number of guesses: ', num_guess)
      else:
        print('Sorry guess is too high')
  elif user_input == 3:
    print()
    print('Thank you for playing')
    print('Goodbye!')
  else:
    print('Incorrect input please select again')
