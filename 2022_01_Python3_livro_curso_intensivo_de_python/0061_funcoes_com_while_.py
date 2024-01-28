### USAR WHILE PARA GERAR UM LOOP INFINITO DE SAUDAÇÃO COM DEVULUÇÃO return

def func_saudacao(nome, sobrenome):
    var_full_name = nome.title() + ' ' + sobrenome.title()
    return var_full_name

while True:
    print('\nPor favor digite seu nome e sobrenome ou "q" para sair: ')
    var_nome = input('\n\tDigite seu nome: ')
    if var_nome == 'q':
        break
    var_sobrenome = input('\n\tDigite seu sobrenome: ') 

    if var_sobrenome == 'q':
        break

    if var_nome or var_sobrenome != 'q':
       var_nome_inteiro = func_saudacao(var_nome, var_sobrenome)
       print('\n\n\t\tNome completo: ' + var_nome_inteiro)

