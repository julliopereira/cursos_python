"""
Métodos úteis dos dicionários em Python
len     - quantas chaves
keys    - iteráveis com as chaves
values  - iteráveis com os valores 
items   - iteráveis com chaves e valores  
setdefault - adiciona valor se a chave não existe
copy    - retorna uma cópia rasa (shallow copy)
get     - obtém uma chave
pop     - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update  - Atualiza um dicionário com outro
"""
# import copy

# #exemplo 1 - len

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'sobrenome1': 'Miranda',
#     'sobrenome2': 'Miranda',
# }

# print(len(pessoa))              # len vai informar quantas chaves temos no dicionario

# #-----------------------------------------------------------------------------
# print('-'*50)
# #-----------------------------------------------------------------------------

# #exemplo 2 - keys

# for chave in pessoa.keys():     # se nao adicionar o metodo keys vai retornar tambem chave 
#     print(chave)                

# #-----------------------------------------------------------------------------
# print('-'*50)
# #-----------------------------------------------------------------------------

# #exemplo 3 - values

# for valor in pessoa.values():     # apenas valores das chaves
#     print(valor)      

# #-----------------------------------------------------------------------------
# print('-'*50)
# #-----------------------------------------------------------------------------

# #exemplo 4 - keys e values 

# for k, v in pessoa.items():     # se nao adicionar o metodo keys vai retornar tambem chave 
#     print(k,':',v)      

# print(list(pessoa.items()))

# #-----------------------------------------------------------------------------
# print('-'*50)
# #-----------------------------------------------------------------------------

# #exemplo 5 - setdefault

# pessoa.setdefault('idade', 0)   # se não existir o valor idade entao coloque zero
# print(pessoa['idade'])

# #exemplo 6 - copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [1, 2, 3]
# }
# d2 = d1.copy()          # copia dicionário (imataveis) d1 para d2; d2 não influencia no d1
# d2['l1'][1] = 9999

# d2['c1'] = 1000

# print(d1)
# print(d2)

# # para fazer uma deep copy necessarios importar copy


# d2['c1'] = copy.deepcopy(d1)


# d2['c1'] = 1000
# d2['l1'][1] = 9999999

# print(d1)
# print(d2)


# # exemplo 7  - get

# p1 = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda'
# }
# print(p1.get('nome'))       # busca valores de dicionarios 

# print(p1.get('nome', 'Não existe!'))       # mostra conteudo da key nome, se nao existir mostra nao existe!

# # exemplo 8  - pop

# nome = p1.pop('nome')       # apaga chave/valor de um dicionario
# print(nome)
# print(p1)

# # exemplo 9  - popitem

# p1 = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda'
# }
# ultima_chave = p1.popitem()       # deleta a ultima chave/valor do dicionario

# print(ultima_chave)
# print(p1)

# # exemplo 10  - update

# p1 = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda'
# }
# p1.update({                     # adiciona um novo chave/valor ao dicionario 
#     'idade': 19,
# })

# print(p1)

# p1.update(peso='42', filme='branca de neve')  # outra forma de adicionar info no dicionario 

# print(p1)

#--------------------------------------------------------------------------------------

#Exercício - sistema de perguntas e respostas


perguntas = [ 
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',        
    },
]

# RESOLUÇÃO 1 - Minha
# acertos = 0
# qde_perguntas = 0
# for item in perguntas:
#     for c, v in item.items():
#         if c == 'Pergunta':
#             print(f'{c}: {v}\n')
#         elif c == 'Opções':
#             print(f'{c}:')
#             for valor in list(v):
#                 print(valor)
#         else:
#             resposta = v
#             escolha = input('Escolha uma opção: ')
#             if v == escolha:
#                 print(f'Acertou :-)')
#                 acertos += 1
#             else:
#                 print(f'Errou X')
        
#     qde_perguntas += 1

# print(f'\nvocê acertou {acertos} \n de {qde_perguntas} pergutas.')

            
# RESOLUÇÃO 2 - Professor

for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'],'\n')

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    qtd_acertos = 0
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print(f'Acertou :-)')
        qtd_acertos += 1
    else:
        print(f'Errou :-(') 

print()
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')


