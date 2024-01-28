### FAÇA UM for COM range() PARA MOSTRAR UMA SEQUÊNCIA DE NÚMEROS

for n in range(1, 6):
    print(n)

### PERCEBA QUE OS NUMEROS SÃO IMPRESSOS ATÉ 5 E NAO ATÉ 6, ESSE COMPORTAMENTO É NORMAL EM PYTHON DEVEMOS CONSIDERAR QUE O ULTIMO VALOR NAO SERÁ IMPRESSO
### FAÇA UM CODIGO ABAIXO QUE FORCE A IMPRESSÃO DE TODOS OS DIGITOS
print('-'*50)
for n in range(1, 6+1):
    print(n)

## TAMBEM PODE SER ASSIM
print('-'*50)
for n in range(1, 7):
    print(n)


### USAR range() PARA MONTAR UMA LISTA DE NUMEROS COM list()
print('-'*50)

numeros = list(range(1, 6))
print(numeros)


### LISTAR NUMEROS PARES NA SEQUENCIA DE 1 A 10 
print('-'*50)

pares = list(range(2, 11, 2))
print(pares)


### ADICIONAR EM UMA LISTA NUMEROS DOBRADOS DE 1 A 10
print('-'*50)

quadrados = []
for valor in range(1, 11):
    quadrado = valor**2
    quadrados.append(quadrado)
print(quadrados)

### O MESMO MAS ADICIONANDO DIRETAMENTE NA PRÓPRIA LISTA:
print('-'*50)
del quadrados

quadrados = []
for valor in range(1, 11):
    quadrados.append(valor**2)
print(quadrados)