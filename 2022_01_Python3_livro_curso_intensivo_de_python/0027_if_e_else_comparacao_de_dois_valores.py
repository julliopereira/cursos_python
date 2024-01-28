### VERIFICANDO IGUALDADE:

'''
Um unico sinal de = quer dizer que está adicionando um valor à uma variável
Dois sinais de == quer dizer que está comparando dois valores

carro = 'bmw'     # ADICIONA VALOR À VARIÁVEL
carro == 'bmw'    # COMPARAÇÃO
'''

carro = 'bmw'
if carro == 'bmw':
    print('Esta é uma BMW')
else:
    print('Esta não é uma BMW')

print('-'*50)
'''
Se a existir diferença de letras maiúsculas e minúsculas 
mude todas para maiusculas ou minusculas na condição para realizar a comparacao
'''

carro = 'Audi'                              # Veja que está declarando audi com a primeira letra maiúscula
if carro == 'audi':                         # E a comparação deste valor está sendo feito com a palavra audi com todas as letras maiusculas
    print('Este carro é um ' + carro)
else:
    print('Este carro não é um audi')       # Neste caso as letras maiusculas e minusculas fazem diferença


print('-'*50)
carro = 'Audi'                              # Veja que está declarando audi com a primeira letra maiúscula
if carro.lower() == 'audi':                 # Agora, na comparação estamos utilizando lower() que vai colcar todas as letras em minusculas
    print('Este carro é um ' + carro)       # Neste caso as letras igualadas vão entrar como iguais
else:
    print('Este carro não é um audi')       


### VERIFICANDO A DIFERANÇA ENTRE DOIS VALORES COM O SINAIL ' != ' 
print('-'*50)

pratos = ['sardinha', 'atum']
for prato in pratos: 
    if prato != 'atum':
         print('Aguarde que já estamos preparando o atum')
    else:
        print('Agora sim, segue o atum')


### TRABALHANDO COM NÚMEROS E OS COMPARANDO:
print('-'*50)

idade = 21
if idade < 21:
    print('Voce tem ' + str(idade) + ' anos, portanto, menor de idade.')
else:
    print('Você tem ' + str(idade) + ' anos, portanto, maior de idade.')



print('-'*50)
### NA VERDADE, QUEM TEM 21 ANOS TAMBÉM DEVE SER CONSIDERADO MENOR PORTANTO VAMOS UTLIZAR <= 
### NO EXEMPLO ANTERIOR QUEM TEM 21 ANOS TAMBÉM É CONSIDERADO MAIOR DE IDADE
if idade <= 21:
    print('Voce tem ' + str(idade) + ' anos, portanto, menor de idade.')
else:
    print('Você tem ' + str(idade) + 'anos, portanto, maior de idade.')