'''
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funcṍes decoradoras em outras funções
'''

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        print('Vou te decorar!')
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Você foi decorada!')
        return resultado
    return interna


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Não é uma string !!!')


def inverte_string(string):
    return string[::-1]


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)


