### PENSE EM 3 TIPOS DE PIZZAS, ARMAZENE OS NOMES E UTILIZE for PARA EXIBIR 

pizzas = ['peperoni', 'mussarela', 'quatro queijos', 'portuguesa', 'calabreza']
for pizza in pizzas:
    print(pizza.title())



### USE for PARA COM UMA FRASE APRESENTAR O NOME DA PIZZA.
### ADICIONE LINHA NO FINAL DE CADA FRASE O QUANTO GOSTOU DA PIZZA
### NO FINAL UMA FRASE SIMPLES.
print('-'*50)
for pizza in pizzas:
    print('A pizza escolhida hoje é "' + pizza.title() + '" \t!')
    print('\t-Adorei a pizza de ' + pizza.title() + '\n')
print('Eu realmente adoro pizza! ')



### PENSE EM TRES ANIMAIS, ARMAZENE E ENTÃO UTILIZE O LAÇO for PARA EXIBIR O NOME DE CADA ANIMAL
### MODIFIQUE O CÓDIGO PARAEXIBIR UMA FRASE PARA CADA ANIMAL 
### NO FINAL UMA FRASE DIZENDO O QUE CADA UM TEM EM COMUM 
print('-'*50)
animais = ['macaco', 'gato', 'cachorro', 'urso', 'leao']
for animal in animais:
    print('O nome do bicho é "' + animal.title() + '" \t!')
print('Todos são mamíferos')
