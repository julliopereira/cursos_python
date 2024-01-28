# CRIAR UMA CALCULADORA QUE FAÇA APENAS DIVISÕES:

print('Me dê dois números divisor e dividendo e farei sua divisão.')
print('Digite "q" para sair.')

while True:
    dividendo = input('\nDividendo: ')
    if dividendo == 'q': 
        break
    divisor = input('Divisor: ')
    if divisor == 'q':
        break
    answer = int(dividendo)/int(divisor)
    print(f'\n\t- A resposta é: {int(answer)}')

