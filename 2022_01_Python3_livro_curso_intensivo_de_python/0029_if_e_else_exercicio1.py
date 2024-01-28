### ESCREVER UM PROGRAMA COM CONDICIONAIS

valores = list(range(1, 20+1))

for v in valores:
    if v < 5:
        print('Valor ' + str(v) + ' < que 5 \n')
    elif v == 5:
        print('Valor ' + str(v) + ' = a 5 \n')
    elif v < 8:
        print('Valor ' + str(v) + ' < que 8 \n')
    elif v == 8: 
        print('Valor ' + str(v) + ' = a 8 \n')
    elif v >= 9 and v <= 15:
        print('Valor ' + str(v) + ' = ' + str(v) + '\n')
    elif v >= 16 and v <= 19:
        print('Valor ' + str(v) + ' = ' + str(v) + '\n')
    elif '21' != v:
        print('Valor ' + str(v) + ' é diferente de 21 \n' )

print('-'*50)
### NOVA LISTA E CONDICIONAIS

carros = ['Ford', 'Volks', 'Audi', 'Gm']
for carro in carros:
    if carro.lower() == 'audi':
        print('Você achou o carro ' + carro.title() + '\n')

print('-'*50)
### SE VALOR ESTÁ EM UMA LISTA
for carro in carros:
    if carro.lower() in 'volks':
        print('Você achou o carro ' + carro.title() + '\n')

print('-'*50)
### SE VALOR NÃO ESTÁ EM UMA LISTA
for carro in carros:
    if carro.lower() not in 'bmw':
        print('BMW não está na lista \n')
        break

