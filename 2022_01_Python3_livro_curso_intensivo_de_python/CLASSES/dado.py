from random import randint

x = randint(1, 6)

class Die():
    def __init__(self,slides=6):
        self.slides = slides

    def rool_die(self):
        count = 1
        print('\n')
        while count <= self.slides:
            x = randint(1, 6)
            print(f'\t  - Jogou:  {x}')
            count += 1

num = int(input('Digite um numero: '))
rolar = Die(num)
rolar.rool_die()