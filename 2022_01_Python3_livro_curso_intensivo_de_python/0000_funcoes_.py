### FUNÇÕES


## VARIADAS

dez = range(2, 10)                          # range     - GRAVE NA VARIAVEL 'dez' OS VALORES DE 2 A 10
print(dez)

inp = input('Digite um valor: ')            # input     - SOLICITA UMA ENTRADA DO USUARIO
inp = int(input('Digite um numero: '))      # int       - O VALOR DIGITADO DEVE SER UM NUMERO INTEIRO
inp = float(input('Digite numero: '))       # float     - O VALOR DIGITADO SERÁ UM NUMERO COM NUMERO FLUTUANTE 
print(type(inp))                            # type      - MOSTRA O TYPE DE VALOR DE UMA VARIAVEL tring inteiro float etc...

## LISTA 

lista = ['honda', 'hyundai', 'gm', 'volks']

print(lista)
print(sorted(lista))                        # sorted    - Em ordem alfabética
print(sorted(lista, reverse=True))          # sorted    - Em ordem alfabética porém inversa sem alterar valores
print(len(lista))                           # len       - Mostra o tamanho da lista (se tiver cinco valores a saída é o número 5) nosso caso 4
print(list(range(1, 6+1)))                  # list      - Com a ajuda de range() pode gerar uma lista com números sequenciais

digitos = list(range(10))
print(min(digitos))                         # min       - Mostra o menor numero da lista
print(max(digitos))                         # max       - Mostra o maior numero da lista
print(sum(digitos))                         # sum       - A soma de todos os dígitos

### DICIONARIO
linguagens_favoritas = {
    'joao': 'python',
    'sara': 'c',
    'eduardo': 'ruby',
    'phil': 'python',
    }

print(linguagens_favoritas.items())                # items     - Mostra todos os itens de um dicionário
print(linguagens_favoritas.keys())                 # keys      - Mostra somente o campo keys (lado esquerdo) 
print(linguagens_favoritas.values())               # values    - Mostra somente o campo values (lado esquerdo)
print(set(linguagens_favoritas.values()))          # set       - Também chamado de conjunto set, torna os valores únicos (python não vai se repetir quando mostrado)

