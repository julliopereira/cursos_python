"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):               # funcao 1
    def saudar(nome):                       # funcao dentro da funcao 1
        return f'{saudacao}, {nome}!'
    return saudar                           # chama funcao saudar - sem parenteses!

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

lista_de_nomes = [ 'Maria', 'Pedro', 'Carlos', 'Fabiana', 'Jéssica', 'Renê', 'Oriovaldo' ]

for nome in lista_de_nomes:
    print(falar_bom_dia(nome))

print('-'*80)
for nome in lista_de_nomes:
    print(falar_boa_noite(nome))
    