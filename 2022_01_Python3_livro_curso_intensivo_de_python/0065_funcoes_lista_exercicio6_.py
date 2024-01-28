# CRIAR UMA LISTA DE NOMES DE MAGICOS E PASSA A LISTA PARA UMA FUNCAO QUE EXIBA O NOME DOS MAGICOS

magicos = ['miranda', 'mauro', 'xman', 'tendu', 'magic']    # CRIANDO LISTA

def show_magicians(magicos):                                # CRIANDO FUNCAO 
    for magico in magicos:
        print(magico)                                       # MOSTRANDO MAGICO

show_magicians(magicos)                                     # CHAMANDO FUNCAO


