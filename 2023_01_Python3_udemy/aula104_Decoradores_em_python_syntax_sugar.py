'''
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funcṍes decoradoras em outras funções

Decoradores são "Syntax Sugar" (açúcar sintático)
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

@criar_funcao                   # chama criar_funcao <<<<<<<< Syntax Sugar
def inverte_string(string):
    return string[::-1]


invertida = inverte_string('123')   # usa a requisicao inicial
print(invertida)


