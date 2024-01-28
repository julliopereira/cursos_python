### LANCHONETE  - CRIAR LISTA DE SANDWICHS E PREENCHER COM NOMES DE SANDWICHES
### MOSTRAR O NOME A MEDIDA QUE FOREM PREPARADOS


sandwich_orders = ['tomate', 'pastrami', 'pichles', 'pastrami', 'queijo prato', 'alface', 'picanha', 'ovo', 'pastrami']
finished_sandwiches = []

print('Preparando os lanches: ')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\tO sandwich de ' + sandwich.title() + ' foi preparado.')
    finished_sandwiches.append(sandwich)

print('\nSandwitchs finalizados: ')
for sandwich in finished_sandwiches:
    print('\tSandwitch pronto: ' + sandwich.title())


print('-'*50) #-----------------------------------------------------------------------------------
### INFORMAR AOS CLIENTES QUE A LANCHONETE ESTA SEM pastrami E REMOVER DA LISTA

sandwich_orders = ['tomate', 'pastrami', 'pichles', 'pastrami', 'queijo prato', 'alface', 'picanha', 'ovo', 'pastrami']
finished_sandwiches = []

print('\nA Loja está sem pastrami !!')
while 'pastrami' in sandwich_orders:                #Q ENQUANTO EXISTIR PASTRAMI NA LISTA USE O COMANDO ABAIXO PARA REMOVER DA LISTA
    sandwich_orders.remove('pastrami')

print('\nPreparando os lanches: ')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\tO sandwich de ' + sandwich.title() + ' foi preparado.')
    finished_sandwiches.append(sandwich)

print('\nSandwitchs finalizados: ')
for sandwich in finished_sandwiches:
    print('\tSandwitch pronto: ' + sandwich.title())



print('-'*50) #-----------------------------------------------------------------------------------
### ENQUETE, QUE LUGAR DO MUNDO VOCÊ GOSTARIA DE VISITAR

respostas = {}

while True:
    nome = input('Qual o seu nome ?: ')
    lugar = input('Que Local do mundo você gostaria de visitar? : ')
    respostas[nome] = lugar
    repetir = input('Gostaria de finalizar a pesquisa?[si/no]: ')
    if repetir == 'no':
        print('---Pesquisa finalizada---')
        break

for nome, resposta in respostas.items():
    print('O senhor(a) ' + nome + '\n\t respondeu ' + resposta)
