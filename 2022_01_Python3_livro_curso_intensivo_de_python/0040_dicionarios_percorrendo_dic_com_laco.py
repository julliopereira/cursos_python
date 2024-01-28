### UTILIZANDO LAÇO PARA PERCORRER A LISTA

'''
É importante entender que para puxar o valor de key e valores
deve-se utilizar o MÉTODO items() que engloba keys() e values() no laço.

E para puxar o valor de key é necessário utilizar o MÉTODO keys() e 
para puxar o valor de values é necessário utilizar values().
'''

print('-'*50)
usuarios = {
    'usuario': 'rodrigo',
    'nome': 'rodrigo',
    'sobrenome': 'pontes',
    }

for k, v in usuarios.items():               # ATRIBUI ÀS VARIÁVEIS k e v OS VALORES PARES DO DICICIONARIO 
    print(str(k) + ':' + str(v))            # MOSTRA O VALOR key e values
print('\n')


### PARA TRABALHAR COM O VALOR keys É NECESSÁRIO UTILIZAR O MÉTODO keys()
print('-'*50)

num_favoritos = { 
    'joao': '30',
    'sara': '10',
    'eduardo': '20',
    'phil': '40',
    }

for nome in num_favoritos.keys():                     # ATRIBUI À VARIÁL nome OS VALORES de NOME
    print('O nome é: ' + str(nome).title())            # MOSTRA O VALOR key 
print('\n')


### PARA TRABALHAR COM O VALOR values É NECESSÁRIO UTILIZAR O MÉTODO values()
print('-'*50)
linguagens_favoritas = {
    'joao': 'python',
    'sara': 'c',
    'eduardo': 'ruby',
    'phil': 'python',
    }

for nome in linguagens_favoritas.values():             # ATRIBUI À VARIÁVEL nome OS VALORES de LINGUAGENS DE PROGRAMAÇÃO
    print('O nome é: ' + str(nome).title())            # MOSTRA O VALOR values 
print('\n')


### NO EXEMPLO ACIMA, BUSCAMOS OS VALORES APENAS COM values() MAS O VALOR python SE REPEDIU
### PARA QUE OS VALOR NÃO SE REPITAM USAMOS O - CONJUNTO set() - QUE SIMPLESMENTE VAI TORNAR O VALOR ÚNICO
print('-'*50)

for nome in set(linguagens_favoritas.values()):             # USANDO O CONJUNTO set()
    print('O nome é: ' + str(nome).title())                 # MOSTRA O VALOR values 
print('\n')
