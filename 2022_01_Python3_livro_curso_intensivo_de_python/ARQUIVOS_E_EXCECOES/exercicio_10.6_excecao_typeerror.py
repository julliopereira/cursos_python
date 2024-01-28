# ESCREVA UM PROGRAMA QUE CALCULE DIVISAO DE DOIS NUMEROS MAS TRATE ENTRADAS TIPO STRING 

print('Me dê dois números divisor e dividendo e farei sua divisão.')
print('Digite "q" para sair.')

while True:
    dividendo = input('\nDividendo: ')
    if dividendo == 'q': 
        break
    divisor = input('Divisor: ')
    try:                                                # EXECUTE A DIVISÃO
        answer = dividendo/divisor
    except TypeError:                                   #
        print('\t- Erro , Você NÃO digitou número !!')       # MOSTRE A MENSAGEM DE ERRO PARA O USUARIO
    except ZeroDivisionError:                           # EXCETO SE DIVIDIR POR ZERO
        print('\t- Não pode dividir por zero !!')       # MOSTRE A MENSAGEM DE ERRO PARA O USUARIO        
    else:
        print(f'\t- A resposta é: {int(answer)}')     # SE NÃO FOR DIVISÃO POR ZERO ENTÃO MOSTRE O RESULTADO DA DIVISÃO