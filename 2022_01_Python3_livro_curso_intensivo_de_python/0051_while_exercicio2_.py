### DIFERENTES VALORES DE PREÇO DE INGRESSO DE ACORDO COM IDADE
### 3 anos = gratuito | 3-12 = 10 dolares | 13 - = 15 dolares

print('Digite sua idade para obter seu ingresso: \n')

while True:
    idade = int(input('\t Digite a idade: '))
    if idade <= 3:
        ingresso = 'gratuito'
        break
    elif idade <= 12:
        ingresso = '10 dolares'
        break
    else:
        ingresso = '15 dolares'
        break

print('\t\tO valor do ingresso é ' + str(ingresso))