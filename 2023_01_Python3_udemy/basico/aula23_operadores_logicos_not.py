# Operadores lógicos
# Usado para inverter expressoes
# not True = False
# not False = True

senha_digitada = input('Senha: ')
senha_permitida = '123456'

if senha_digitada != senha_permitida:
    print('Sair')


# curto circuito
print(not True) #False
print(not False) #True


