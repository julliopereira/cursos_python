### DIFERENTE DO LAÇO for O LAÇO while EXECUTA ENQUANTO O USUARIO QUISER PERMANECER NELE

contador = 1

while contador <= 5:                                        # SE O CANTADOR MENOR OU IGUAL A CINCO FAÇA O QUE ESTÁ DENTRO DE while
    print('contador: ' + str(contador) + ' menor que 6')
    contador += 1


print("-"*50) #---------------------------------------------------------------------
#### USURIO VAI DIGITAR VÁRIAS PALAVRAS A SEREM MOSTRADAS NA TELA, MAS SÓ VAI SAIR DO while QUANDO DIGITAR quit

dig = 'Digite qualquer coisa para eu mostrar'
dig += '\tDigite "quit" para encerrar'

mensagem = ''

while mensagem != 'quit':
    mensagem = input('Digite mensagem: ')
    print(mensagem)

print("-"*50) #---------------------------------------------------------------------
#### PARA NÁO MOSTRAR O QUIT NO FINAL USAR UM if SIMPLES

mensagem = ''
while mensagem != 'quit':
    mensagem = input('Digite mensagem: ')
    if mensagem != 'quit':
        print(mensagem)

print("-"*50) #---------------------------------------------------------------------
#### USANDO UMA flag QUE É UMA VARIAVEL QUE DEVE SER ALTERADA SE QUISER SAIR DO while

bandeira = True

while bandeira:                                        
    texto = input('Digite qualquer coisa ou quit para sair: ')
    if texto == 'quit':
        bandeira = False

print("-"*50) #---------------------------------------------------------------------
#### USANDO A INSTRUÇÃO break PARA PARAR O LAÇO ONDE ESTIVER



while True:                                        # O true FAZ UM LAÇO ETERNO ATÉ QUE O break SEJA EXECUTADO
    texto = input('Digite qualquer coisa ou quit para sair2: ')
    if texto == 'quit':
        break
    else:   
        print(texto)


print("-"*50) #---------------------------------------------------------------------
####  USANDO A FUNÇÃO continue PARA RETORNAR AO INICIO DO LOOP

num = 0

while num < 10:  
    num += 1
    if num % 2 == 0:                            # SE O RESTO DA DIVISAO DE Num POR 2 FOR IGUAL A ZERO 
        continue                                # RETORNE IMEDIATAMENTE PARA O COMEÇO DO WHILE
    
    print('o número ' + str(num) + ' é ímpar') 
