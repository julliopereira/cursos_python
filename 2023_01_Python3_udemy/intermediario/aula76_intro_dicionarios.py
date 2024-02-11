"""
Dicionarios em Python (tipo dict)
Dicionarios sao estrutura de dados do tipo 
par de "chave" e "valor"

Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.

O valor pode ser de qulquer tipo, incluindo outro dicionário.

Usamos as chaves - {} - ou a classe dict para criar 
dicionarios

Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

pessoa = { 
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [ 
        {'rua': 'tal tal', 'numero': 123}
        {'rua': 'outra rua', 'numero': 234}
    ]
}

print(pessoa, type(pessoa))

"""

# exemplo 1 de criacao de dicionario
# pessoa = { 
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'enderecos': [ 
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 234},
#     ]
# }

# print(pessoa, type(pessoa))

# for k, v in pessoa.items():
#         print(f'{k}:{v}')

#-----------------------------------------------

# exemplo 2 de criacao de dicionario

# pessoa = dict(nome='Julio', idade='41')
# print(pessoa)

#-----------------------------------------------

# exemplo 3 

# pessoa = {}

# pessoa['nome'] = 'Luiz Otávio'      # Adiciona key=nome value=Luiz Otávio no dicionario pessoa

# print(pessoa['nome'])               # Acessar o conteudo de nome do dicionario pessoa

#-----------------------------------------------

# exemplo 4

pessoa = {}                         # declara o dicionario

chave = 'nome'

pessoa[chave] = 'Julio Cesar'       # Adiciona valor a chave nome
pessoa['sobrenome'] = 'Pereira'     # Adiciona valor a chave sobrenome

print(pessoa[chave])                # Mostra o conteúdo da chave nome

pessoa[chave] = 'Maria'             # Atribui valor Maria a chave nome

del pessoa['sobrenome']             # Deleta a chave sobrenome
print(pessoa)                       # Mostra o conteudo do dicionario pessoa
print(pessoa['nome'])               # Mostra o conteúdo da chave nome

if pessoa.get('sobrenome') is None: # metodo get() tenta obter valor - se retornar None - entao Nao existe
    print('Não existe')
else:
    print(pessoa['sobrenome'])

print('tratado erro acima com get o código continua')