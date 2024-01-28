"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro
"""
# solucao 1
# try:
#     numero_int = int(input('Digite um numero inteiro: '))
#     resultado_divisao_por_dois = numero_int % 2
#     if resultado_divisao_por_dois == 0:
#         print(f'Numero {numero_int} é par')
# except:
#     print('\n\nNão é número inteiro!!')

# solucao 2 - professor

# entrada = input('Digite um numero inteiro: ')
# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

# try: 
#     hora_atual = int(input('Digite a hora atual: '))
#     minuto_atual = int(input('Digite minuto atual: '))
#     if hora_atual >= 0 and hora_atual <= 11:
#         print('Bom dia!')
#     elif hora_atual >= 12 and hora_atual <= 17:
#         print('Boa tarde!')
#     elif hora_atual >= 18 and hora_atual <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora!')
# except:
#     print('não digitou corretamente')

"""
Faça um programa que peça o primeiro nome do usuário, Se o nome tiver 4 letras ou 
menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

primeiro_nome = input('Digite seu primeiro nome: ')
tamanho_do_nome = len(primeiro_nome)
print('\n')

if primeiro_nome > 1:
    if tamanho_do_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_do_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
