"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""

# minha solucao 
# def criar_multiplicador(numero):
#     def triplica():
#         def quadruplica():
#             quadruplicado = numero * 4
#             return f'O {numero=},{duplicado=}, {triplicado=} e {quadruplicado=}'
#         triplicado = numero * 3
#         return quadruplica()
#     duplicado = numero * 2    
#     return triplica()         

# print(criar_multiplicador(20))

#----------------------------------------------------------
# solucao professor - legal

# [1] criar funcoes chando funcoes
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

# [2] chamar primeira funcao passando o multiplicador
duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

# [3] chamar a variavel correspondente ao multiplicador com o valor a ser multiplicado e mostrar na tela
print(duplicar(20))
print(triplicar(40))
print(quadriplicar(60))
