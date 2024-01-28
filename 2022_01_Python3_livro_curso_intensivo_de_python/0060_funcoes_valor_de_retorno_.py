### return DEVOLTE PARA QUEM CHAMA O VALOR FINAL DE UMA FUNÇÃO

print('-'*50)#------------------------------------------------------------------------------
print('EX 1:')


def func_nome_formatado(first_name, last_name):
    """Devolve um nome compleso usando return"""
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name                                          # RETORNA O VALOR DE full_name PARA A STRING QUE CHAMOU A FUNÇÃO

musico = func_nome_formatado('jimi', 'hendrix')               # ADICIONA O CONTEÚDO DE return NA VARIAVEL musico
print(musico)

print('-'*50)#------------------------------------------------------------------------------
### UMA STRING VAZIA ( DEVE SER COLOCADA NO FINAL DA FUNÇÃO )
print('EX 2:')

def func_nome_formatado2(first_name, last_name, midle_name=''):
    """Devolve um nome compleso usando return"""
    full_name = first_name.title() + ' ' + midle_name + ' ' + last_name.title()
    return full_name                                          

musico = func_nome_formatado2('john', 'lee', 'hooker')               
print(musico)

musico = func_nome_formatado2(first_name='john', last_name='hooker')               # PODE NÁO ADD UM ARGUMENTO MAS TEM QUE DEFINIR AS DEMAIS
print(musico)                                                                      
