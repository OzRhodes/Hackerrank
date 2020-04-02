#guessinggame.py

import random

def guess(guessed_num, answer):
    if guessed_num > answer:
        response = 'The number is lower.\n'
    else:
        response = 'The number is higher.\n'
    return response


answer = str(random.randint(1,20))
guessed_num = ''
while True:
    guessed_num = input('Enter your Guess: ')
    if guessed_num != answer:
        print(guess(guessed_num, answer))
    else:
        print('Youŕe correct the number is: {} \n'.format(answer))
        break



