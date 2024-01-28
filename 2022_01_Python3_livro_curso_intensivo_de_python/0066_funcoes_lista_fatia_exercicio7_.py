# CRIAR UMA LISTA DE NOMES DE MAGICOS E PASSA A LISTA PARA UMA FUNCAO QUE EXIBA O NOME DOS MAGICOS

magicos = ['miranda', 'mauro', 'xman', 'tendu', 'magic']    # CRIANDO LISTA

def show_magicians(magicos):                                # CRIANDO FUNCAO 
    for magico in magicos:
        print(magico)                                       # MOSTRANDO MAGICO

def make_great(magicos):                                    # FUNCAO QUE ALTERA O VALOR DE CADA ENTRADA COM + O Grande no final
    c = 0
    for magico in magicos:
        nome = magico + " O Grande!"
        magicos[c] = nome
        c += 1
        print(magicos)

make_great(magicos[:])                                      # [:] Faz uma cópia e não altera o original


print('\n\nChamando lista após make_great alterar informacoes: \n')
show_magicians(magicos)                                     # CHAMANDO FUNCAO