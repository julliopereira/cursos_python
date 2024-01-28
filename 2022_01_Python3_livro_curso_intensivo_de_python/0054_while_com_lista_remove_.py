### REMOVER UM NOME QUE SE REPETE VÁRIAS VEZES EM UMA LISTA 

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)
